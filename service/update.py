import json
from requests import get
from PyQt5.QtCore import QThread, pyqtSignal
from constants import VERSION_CODE, VERSION_NAME
from constants import USERAGENT


def checkUpdate():
    """ 返回最新的版本名，版本号 """
    version_name = VERSION_NAME
    version_code = VERSION_CODE

    update_url = "https://alpherk.github.io/NjtechAutoLogin/release/versions.json"
    get_header = {'User-Agent': USERAGENT}
    
    try:
        get_json = get(url=update_url, headers=get_header).text
        jsondata = json.loads(get_json)

        for ver in jsondata:
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
            self.update_info.emit(version_name, "确定")
        else:
            self.update_info.emit(version_name, "下载")


if __name__ == '__main__':

    print(checkUpdate())