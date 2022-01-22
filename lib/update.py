import json
from PyQt5.QtCore import QThread, pyqtSignal
from lib.constants import VERSION_CODE, VERSION_NAME


def checkUpdate():
    """ 返回最新的版本名，版本号 """
    version_data = [
                { "versionApp": "1.2.2" , "versionCodeApp": 122},
                { "versionWin": "6.2.9" , "versionCodeWin": 621},
                { "version": "1.1.0" , "versionCode": 110},
                { "version": "1.0.0" , "versionCode": 100}
            ]
    jsondata = json.dumps(version_data)
    jsondata = json.loads(jsondata) #读取json文件流

    version_name = VERSION_NAME
    version_code = VERSION_CODE

    for ver in jsondata:
        try:
            if (version_code < ver['versionCodeWin']):
                version_code = ver['versionCodeWin']
                version_name = ver['versionWin']
        except: pass
    if (version_code == VERSION_CODE):
        """ 当前为最新版 """
        version_code = 0

    return version_name, version_code


class BackThread(QThread):
    """ 后台检查版本更新 """
    update_info = pyqtSignal(str, str)
    
    def run(self):

        version_name, version_code = checkUpdate()
        if (version_code == 0):
            check_tip = f"已更新至最新版本：{version_name}"
            self.update_info.emit(check_tip, "确定")
        else: 
            check_tip = f"最新版本为：{version_name}，是否自动跳转至浏览器下载？"
            self.update_info.emit(check_tip, "下载")