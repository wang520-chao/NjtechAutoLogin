from requests import get, post
from re import search
from time import time, sleep


################## 读取登录密码 ####################
def get_userword():
    userword = []
    for line in open("build/Auto_login/userword.txt"): 
        line = line.strip('\n')
        userword.append(line)
    return userword

def get_channel():
    if userword[2]   == '  中国移动':
        channel = ['中国移动',    '@cmcc']
    elif userword[2] == '  中国电信':
        channel = ['中国电信', '@telecom']
    return channel

def isConnected():
    try:
        html = get("http://www.baidu.com",timeout=1)
    except:
        return False
    return True

def post_req(userword, channel):
    ############ 发送get请求, 获取post所需数据 ##########
    url = "https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232"
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'

    get_headers = {'User-Agent':    useragent}
    njtech = get(url=url, headers=get_headers)
    njtech = njtech.text
    lt  = search("name=\"lt\" value=\"(.*?)\"",        njtech)
    exe = search("name=\"execution\" value=\"(.*?)\"", njtech)
    js  = search("jsessionid=(.*?)\">",                njtech)

    lt  =  lt.groups()[0]
    exe = exe.groups()[0]
    cookies = 'JSESSIONID=' + js.groups()[0] + '; insert_cookie=97324480'

    ############# 发送post请求, 完成认证 ################
    post_header = {
        "Cookie":       cookies,
        "User-Agent":   useragent,
    }
    post_data = {
        "username":     userword[0],
        "password":     userword[1],
        "channelshow":  channel[0],
        "channel":      channel[1],
        "lt":           lt,
        "execution":    exe,
        "_eventId":     "submit",
        "login":        "登录",
    }
    request = post(url=url, data=post_data, headers=post_header)
    

start = time()
print('\n  >>>>> 开始自动登录 ')
userword = get_userword()
channel  = get_channel()

post_req(userword, channel)

if isConnected() == False:
    post_req(userword, channel)
    print('\n  >>>>> 遇到问题啦, 正在重连中')


print('\n  >>>>> 恭喜您, 完成认证 ')
end = time()
print('\n  登录所需共用时%.2f秒' %(end-start))
print('\n  窗口将在 1s 内退出, 谢谢使用')
sleep(1)

