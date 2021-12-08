import re
import os
import sys
from enum import Enum
from urllib.parse import urlencode, quote_plus, unquote
import requests
from flask import Flask, request, redirect, jsonify, abort, make_response
# from waitress import serve

app = Flask(__name__)
ORIGIN = 'http://pan.lanzou.com'


class Client(Enum):
    PC = 1
    MOBILE = 2


def gen_headers(client: Client):
    return {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': ORIGIN,
        'User-Agent': [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'
        ][0 if client == Client.PC else 1]
    }


def get(url, client: Client):
    return requests.get(url, headers=gen_headers(client), allow_redirects=False)


def post_data(url, data, client: Client):
    return requests.post(url, data, headers={
        **gen_headers(client),
        'Content-Type': 'application/x-www-form-urlencoded'
    })


def find_first(pattern, text):
    match = re.findall(pattern, text)
    if match:
        return match[0]


def get_params(fid: str, client: Client, pwd=None):
    if client == Client.PC:
        text = get(f'{ORIGIN}/{fid}', client).text
        if pwd:
            params = find_first(r"[^/]{2,}data : '(.+)'\+pwd", text) + pwd
        else:
            fn = find_first(r'src="(.{20,})" frameborder', text)
            text = get(f'{ORIGIN}/{fn}',  client).text

            try:
                exec(find_first(
                    r"[^/]{2,}var (.+ = '\?[\w/_+=]{1,10}')", text))
                exec(find_first(r"[^/]{2,}var (.+ = '[\w/_+=]{20,}')", text))
            except Exception:
                pass

            data = eval(find_first(r"[^/]{2,}data : ({.+})", text))
            params = urlencode(data, quote_via=quote_plus)

    else:
        if not fid.startswith('i'):
            text = get(f'{ORIGIN}/{fid}', client).text
            fid = find_first(r"[^/]{2,}.+ = 'tp/(.+)'", text)

        text = get(f'{ORIGIN}/tp/{fid}', client).text

        if pwd:
            params = eval(find_first(r"[^/]{2,}data : ({.+})", text))
        else:
            url_pre = find_first(r"[^/]{2,}.+ '(http[\w:/\-\.]{10,})'", text)
            url_suf = find_first(r"[^/]{2,}.+ '(\?[\w/+=]{100,})'", text)
            params = url_pre + url_suf
    return params


def get_url(fid, client: Client, pwd=None):
    params = get_params(fid, client, pwd)
    if client == Client.MOBILE and not pwd:
        response = get(params, client)
    else:
        result = post_data(f'{ORIGIN}/ajaxm.php', params, client).json()
        fake_url = f"{result['dom']}/file/{result['url']}"
        response = get(fake_url, client)

    return response.headers['location']


def fmt_size(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)


def get_full_info(url):
    headers = requests.head(url, allow_redirects=False).headers
    return {
        'name': unquote(headers.get('Content-Disposition').split('filename= ')[-1]),
        'size': fmt_size(int(headers.get('Content-Length'))),
        'url': url,
    }


def gen_json_response(code, msg, extra={}):
    return make_response(jsonify({
        'code': code,
        'msg': msg,
        **extra
    }))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if not re.match('.+\?.*url=.*lanzou.*\.com%2F[\w]{4,}.*', request.url):
        return gen_json_response(
            -1,
            'invalid link',
            {
                'examples': [
                    f'{request.base_url}?url={ORIGIN}/i4wk2oh&type=down',
                    f'{request.base_url}?url={ORIGIN}/i7tit9c&pwd=6svq&type=json',
                ]
            }
        )

    url = request.args.get('url')
    pwd = request.args.get('pwd')
    data_type = request.args.get('type')
    fid = url.split('/')[-1]

    errors = []
    for client in [Client.MOBILE, Client.PC]:
        try:
            url = get_url(fid, client, pwd)
            if url.find('dev') < 0:
                continue

            if data_type == 'down':
                return redirect(url)
            else:
                return gen_json_response(
                    200,
                    'success',
                    {'data': get_full_info(url)}
                )
        except Exception as e:
            errors.append(e)
            pass

    abort(500, errors)


@app.errorhandler(500)
def server_error(error):
    return gen_json_response(
        -2,
        'link not match pwd, or lanzous has changed their webpage',
        {'detail': str(error)}
    )


@app.after_request
def cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


def test():
    def request(fid, client: Client, pwd=None):
        print(f'fid={fid}, client={client}, pwd={pwd}')
        print(get_url(fid, client, pwd))
        print('--------------------------------------')

    request('i7tit9c', Client.MOBILE, '6svq')
    request('i7tit9c', Client.PC, '6svq')
    request('i4wk2oh', Client.MOBILE)
    request('i4wk2oh',  Client.PC)
    request('iRujgdfrkza', Client.MOBILE)
    request('iRujgdfrkza', Client.PC)
    # request('feifei1', Client.MOBILE, 'aam1')
    # request('feifei1', Client.PC, 'aam1')
    request('dkbdv7', Client.MOBILE)
    request('dkbdv7', Client.PC)


if __name__ == '__main__':
    port = int(os.getenv('PORT', '3000'))
    if len(sys.argv) <= 1 or sys.argv[1] != 'production':
        test()
        app.config['JSON_AS_ASCII'] = False
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    # else:
        # serve(app, host='127.0.0.1', port=port)

    app.run(host='127.0.0.1', port=port)