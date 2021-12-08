from requests import get, post
from re import search
from time import time, sleep
start = time()
print('  >>>>> 开始自动登录 ')
################## 读取登录密码 ####################
def userword():
    userword = []
    for line in open("userword.txt"): 
        line = line.strip('\n')
        userword.append(line)
    return userword
userword = userword()

############ 发送get请求, 获取post所需数据 ##########
url = "https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232"
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'

get_headers = {'User-Agent': useragent}
njtech = get(url=url, headers=get_headers)
njtech = njtech.text
lt = search("name=\"lt\" value=\"(.*?)\"", njtech)
exe = search("name=\"execution\" value=\"(.*?)\"", njtech)
js = search("jsessionid=(.*?)\">", njtech)


############### 处理后的post所需数据 ################
lt = lt.groups()[0]
exe = exe.groups()[0]
cookies = 'JSESSIONID=' + js.groups()[0] + '; insert_cookie=97324480'


############# 发送post请求, 完成认证 ################
post_header = {
    "Cookie": cookies,
    "User-Agent": useragent,
}
post_data = {
    "username": userword[0],
    "password": userword[1],
    "channelshow": "中国移动",
    "channel": "@cmcc",
    "lt": lt,
    "execution": exe,
    "_eventId": "submit",
    "login": "登录",
}

req = post(url=url, data=post_data, headers=post_header)

print('  >>>>>  完成认证 ')
end = time()
print('  登录所需共用时%.2f秒' %(end-start))
sleep(3)

