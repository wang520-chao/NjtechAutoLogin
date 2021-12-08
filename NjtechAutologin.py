import sys
from configparser import ConfigParser
from os import getcwd
from webbrowser import open_new_tab
import win32api
import win32con
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from build import LoginUI, MainUI, RewardUI, resource
from lib.utils import *
class WdoLogin(QWidget):

    def __init__(self):

        super(WdoLogin, self).__init__()
        self.ui = LoginUI.Ui_Form()
        self.ui.setupUi(self)
        try: self.loadLoginData()
        except: pass

        # 设置登录配置事件
        self.ui.ckbx_pwrboot.stateChanged.connect(self.powerBoot)
        self.ui.ckbx_showlogin.stateChanged.connect(self.showLoginInfo)
        self.ui.spbox_cnct_time.valueChanged.connect(self.btnLink)

        # 点击登录按钮事件
        self.ui.btn_login.clicked.connect(self.saveLoginData)
        self.ui.ed_pwd.returnPressed.connect(self.saveLoginData)

        # 底部信息处理事件
        self.ui.btn_feedback.clicked.connect(self.jumpFeedBack)
        self.ui.btn_upgrade.clicked.connect(self.jumpGetUpgrade)
        self.ui.btn_givereward.clicked.connect(self.jumpGiveReward)


    def saveLoginData(self):

        self.username  = self.ui.ed_usr.text()
        self.password  = self.ui.ed_pwd.text()
        self.channel   = self.ui.cbbx_channel.currentText()
        self.powerboot = self.ui.ckbx_pwrboot.isChecked()
        self.showlogin = self.ui.ckbx_showlogin.isChecked()
        self.reconnect = self.ui.spbox_cnct_time.value()

        mkConfigDir()   # 创建若不存在
        config = ConfigParser()
        config[LOGIN_DATA_WARN1] = {}
        config[LOGIN_DATA_WARN2] = {}
        config[LOGIN_PART_1] = {
            LOGIN_DATA_1: self.username,
            LOGIN_DATA_2: self.password,
            LOGIN_DATA_3: self.channel }
        config[LOGIN_PART_2] = {
            LOGIN_DATA_4: self.powerboot,
            LOGIN_DATA_5: self.reconnect,
            LOGIN_DATA_6: self.showlogin}
        with open(LoginFile_Path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)


    def loadLoginData(self):
        self.config = ConfigParser()
        self.config.read(LoginFile_Path, encoding='utf-8')
        self.username  = self.config[LOGIN_PART_1][LOGIN_DATA_1]
        self.password  = self.config[LOGIN_PART_1][LOGIN_DATA_2]
        self.channel   = self.config[LOGIN_PART_1][LOGIN_DATA_3]
        self.powerboot = self.config[LOGIN_PART_2][LOGIN_DATA_4]
        self.reconnect = self.config[LOGIN_PART_2][LOGIN_DATA_5]
        self.showlogin = self.config[LOGIN_PART_2][LOGIN_DATA_6]
        self.reconnect = int(self.reconnect)

        self.ui.ed_usr.setText(self.username)
        self.ui.ed_pwd.setText(self.password)
        self.channel_index = 0 if self.channel=='中国移动' else 1
        self.ui.cbbx_channel.setCurrentIndex(self.channel_index)
        self.ui.spbox_cnct_time.setValue(self.reconnect)

        if self.powerboot == 'True':
            self.ui.ckbx_pwrboot.setChecked(True)
        if self.showlogin == 'True':
            self.ui.ckbx_showlogin.setChecked(True)

        self.powerBoot()


    def showLoginInfo(self):
        if self.ui.ckbx_showlogin.isChecked():
            # 屏蔽复选框点击事件 21.10.04
            pass


    def powerBoot(self):
        path = getcwd() + f"\\{AutoLogin_EXE}"
        runpath = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_ALL_ACCESS)

        if self.ui.ckbx_pwrboot.isChecked():
            win32api.RegSetValueEx(hKey, AutoLogin_EXE, 0, win32con.REG_SZ, path)
        else:
            try: win32api.RegDeleteValue(hKey, AutoLogin_EXE)
            except: pass
        win32api.RegCloseKey(hKey)


    def btnLink(self):
        if int(self.ui.spbox_cnct_time.value()) > -1:
            self.ui.ckbx_pwrboot.setChecked(True)
            self.ui.ckbx_showlogin.setChecked(False)


    def jumpFeedBack(self):
        WdoController.mainWdo = WdoMain()
        WdoController.mainWdo.show()


    def jumpGiveReward(self):
        WdoController.mainWdo = GiveReward()
        WdoController.mainWdo.show()

    @staticmethod
    def jumpGetUpgrade():
        upgrade_url = CSDN_PROJECT_URL
        open_new_tab(upgrade_url)


class WdoMain(QMainWindow):
    def __init__(self):
        super(WdoMain, self).__init__()
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(WdoLogin.jumpGetUpgrade)


class GiveReward(QMainWindow):
    def __init__(self):
        super(GiveReward, self).__init__()
        self.ui = RewardUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(WdoLogin.jumpGetUpgrade)


class WdoController:
    loginWdo = None
    mainWdo  = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    WdoController.loginWdo = WdoLogin()
    WdoController.loginWdo.show()
    sys.exit(app.exec_())


