from selenium.webdriver import Edge, EdgeOptions
from time import sleep
from socket import socket
from warnings import filterwarnings
filterwarnings("ignore")

url = "https://i.njtech.edu.cn/index.html"  # 南工校园网网址
user_xpath = '//*[@id="username"]'
pwd_xpath = '//*[@id="password"]'
channel_xpath = '//*[@id="channelshow"]'
cmcc_xpath = '//*[@id="fm1"]/div/div[1]/div[1]/div[4]/div/span[2]'
button_xpath = '//*[@id="login"]'

driver_url = r"..\build\msedgedriver.exe"
options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
driver = Edge(executable_path=driver_url, options=options)

def userword():
    userword = []
    for line in open("userword.txt"): 
        line = line.strip('\n')
        userword.append(line)
    return userword

def AutoLogin(url, username, passwd,
    user_xpath, pwd_xpath, channel_xpath,
    cmcc_xpath, button_xpath):

    print("\n  >>> 启动认证中")
    driver.maximize_window() 
    driver.implicitly_wait(6)   # 6秒内找到元素则立即执行
    driver.get(url)             # 获取网页
    sleep(0.1)
    
    print("\n  >>> 填充密码中")
    # 通过xpath找到文本框并传入文本
    driver.find_element_by_xpath(user_xpath).send_keys(username)
    driver.find_element_by_xpath(pwd_xpath).send_keys(passwd)
    sleep(0.1)
    
    print("\n  >>> 正在登陆中")
    # 点击校园网按钮 -> 点击中国移动 -> 点击登录按钮
    try:
        driver.find_element_by_xpath(channel_xpath).click()
        driver.find_element_by_xpath(cmcc_xpath).click()
    except:
        pass
    driver.find_element_by_xpath(button_xpath).click()

    print("\n  >>> 登录成功 !!")
    driver.quit()       # 登录后关闭浏览器

userword = userword()

AutoLogin(
    url=url,
    username=userword[0],
    passwd=userword[1],
    user_xpath=user_xpath,
    pwd_xpath=pwd_xpath,
    channel_xpath=channel_xpath,
    cmcc_xpath=cmcc_xpath,
    button_xpath=button_xpath)

