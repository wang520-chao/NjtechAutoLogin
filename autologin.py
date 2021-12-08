import threading
from configparser import ConfigParser
from os.path import dirname, realpath
from re import search
from sys import argv
from time import sleep, time
from requests import get, post
from lib.utils import *


################## 南工大自动登录 ####################

class AutoLogin:

    def __init__(self):
        try: self.getLoginData()
        except: saveLogFile()


    def getLoginData(self):
        self.info = {}
        self.config = ConfigParser()
        self.config.read(dirname(realpath(argv[0])) + LoginFile_Path, encoding='utf-8')
        self.info['cnt'] = int(self.config[LOGIN_PART_2][LOGIN_DATA_5].strip())
        self.info['usr'] = self.config[LOGIN_PART_1][LOGIN_DATA_1].strip()
        self.info['pwd'] = self.config[LOGIN_PART_1][LOGIN_DATA_2].strip()
        self.info['shw'] = self.config[LOGIN_PART_1][LOGIN_DATA_3].strip()
        if   self.info['shw'] == '中国移动':   self.info['nel'] = '@cmcc'
        elif self.info['shw'] == '中国电信':   self.info['nel'] = '@telecom'


    def requestLogin(self):

        ############ 发送get请求, 获取post所需数据 ##########
        url_host  = "https://u.njtech.edu.cn/cas/login"
        url_query =("?service=https://u.njtech.edu.cn/oauth2/authorize"
                    "?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code"
                    "&state=njtech&s=f682b396da8eb53db80bb072f5745232" )
        useragent =("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41")
        get_headers = {'User-Agent':          useragent}
        get_url = url_host + url_query
        njtech  = get(url=get_url, headers=get_headers).text

        lt      = search('lt\" value=\"(.*?)\"',        njtech).groups()[0]
        exe     = search('execution\" value=\"(.*?)\"', njtech).groups()[0]
        js      = search('jsessionid=(.*?)\">',         njtech).groups()[0]
        cookies = F"JSESSIONID={js}; insert_cookie=97324480"

        ############# 发送post请求, 完成认证 ################
        post_url = F"{url_host};jsessionid={js}{url_query}"
        post_header = {
            "Cookie":               cookies,
            "User-Agent":         useragent}
        post_data = {
            "username":    self.info['usr'],
            "password":    self.info['pwd'],
            "channelshow": self.info['shw'],
            "channel":     self.info['nel'],
            "lt":                        lt,
            "execution":                exe,
            "_eventId":            "submit",
            "login":                 "登录"}
        post(url=post_url, headers=post_header, data=post_data)


    def toConnect(self):
        threads = []
        threads.append(threading.Thread(target=self.requestLogin))
        threads.append(threading.Thread(target=connectionProcessBar))
        for t in threads: t.start()
        for t in threads: t.join()


    def reConnect(self):
        for i in range(11):
            if internetIsConnected(): break
            else:
                print('\r\t＞﹏＜ 出错啦 ~ 正在拼命重连中 ~   第{0}次重连 ~ '.format(i+1))
                self.toConnect()
            if i == 11: failConnectTost()


    def intervalConnect(self):
        while self.info['cnt'] > -1:
            self.reConnect()
            print("运行中")
            print(self.info['cnt'])
            sleep(self.info['cnt'])
        print("重连间隔时间 < 0, 程序退出")
        sleep(3)



if __name__ == '__main__':

    start = time()

    login = AutoLogin()
    login.toConnect()
    login.reConnect()

    end = time()

    sucsConnectToast(end-start)

    login.intervalConnect()




