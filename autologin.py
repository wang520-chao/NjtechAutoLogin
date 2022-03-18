from configparser import ConfigParser
from os.path import dirname, realpath
from re import search
from sys import argv
from threading import Thread
from time import sleep, time

from requests import get, post

from service import utils
from service.constants import *

################## 南工大自动登录 ####################

class AutoLogin:

    def __init__(self):
        try: self.getLoginData()
        except: utils.saveLogFile()

    def getLoginData(self):
        self.info = {}
        self.config = ConfigParser()
        self.config.read(dirname(realpath(argv[0])) + LOGINFILE_PATH, encoding='utf-8')
        self.info['cnt'] = int(self.config[LOGIN_PART_2][LOGIN_DATA_5].strip())
        self.info['usr'] = self.config[LOGIN_PART_1][LOGIN_DATA_1].strip()
        self.info['pwd'] = self.config[LOGIN_PART_1][LOGIN_DATA_2].strip()
        self.info['shw'] = self.config[LOGIN_PART_1][LOGIN_DATA_3].strip()
        if   self.info['shw'] == '中国移动':   self.info['nel'] = '@cmcc'
        elif self.info['shw'] == '中国电信':   self.info['nel'] = '@telecom'

    def requestLogin(self):

        ############ 发送get请求, 获取post所需数据 ##########
        url_hosts = "https://u.njtech.edu.cn/cas/login"
        url_query =("?service=https://u.njtech.edu.cn/oauth2/authorize"
                    "?client_id=Oe7wtp9CAMW0FVygUasZ&response_type=code"
                    "&state=njtech&s=f682b396da8eb53db80bb072f5745232" )
        get_urls = url_hosts + url_query
        get_head = {'User-Agent': USERAGENT}
        get_info = get(url=get_urls, headers=get_head).text

        lt      = search('lt\" value=\"(.*?)\"',        get_info).groups()[0]
        exe     = search('execution\" value=\"(.*?)\"', get_info).groups()[0]
        js      = search('jsessionid=(.*?)\">',         get_info).groups()[0]
        cookies = F"JSESSIONID={js}; insert_cookie=97324480"

        ############# 发送post请求, 完成认证 ################
        post_urls = F"{url_hosts};jsessionid={js}{url_query}"
        post_head = {
            "Cookie":               cookies,
            "User-Agent":         USERAGENT}
        post_data = {
            "username":    self.info['usr'],
            "password":    self.info['pwd'],
            "channelshow": self.info['shw'],
            "channel":     self.info['nel'],
            "lt":                        lt,
            "execution":                exe,
            "_eventId":            "submit",
            "login":                 "登录"}
        post(url=post_urls, headers=post_head, data=post_data)

    def toConnect(self):
        threads = []
        threads.append(Thread(target=self.requestLogin))
        threads.append(Thread(target=utils.connectionProcessBar))
        for t in threads: t.start()
        for t in threads: t.join()

    def reConnect(self):
        for i in range(11):
            if utils.internetIsConnected(): break
            else:
                print('\r\t＞﹏＜ 出错啦 ~ 正在拼命重连中 ~   第{0}次重连 ~ '.format(i+1))
                self.toConnect()
            if i == 11: utils.failConnectTost()

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

    utils.sucsConnectToast(end-start)

    login.intervalConnect()




