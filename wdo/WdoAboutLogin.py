import sys
from webbrowser import open_new_tab
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from lib.update  import *
from lib.utils import *
from lib.constants import DOWN_URL, SOFT_ZIP
from wdo import FeedbackUI, RewardUI, DialogUI


class WinFeedback(QMainWindow):
    """ 反馈说明界面 """

    def __init__(self):
        super(WinFeedback, self).__init__()
        self.ui = FeedbackUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(jumpMyCSDN)


class WinGiveReward(QMainWindow):
    """ 打赏点赞界面 """

    def __init__(self):
        super(WinGiveReward, self).__init__()
        self.ui = RewardUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(jumpMyCSDN)


class WinUpdateDialog(QDialog):
    """ 检查更新界面 """

    def __init__(self) -> None:
        super(WinUpdateDialog, self).__init__()
        self.ui = DialogUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶窗口
        self.checkUpdate()

    def checkUpdate(self):
        """ 检查软件更新 """
        self.ui.textbrow_info.setText("检查更新中···")
        self.backend = BackThread() #后台检查更新
        self.backend.update_info.connect(self.updateDisplay)
        self.backend.start()
    
    def updateDisplay(self, info, yes_btn):
        """ 更新界面信息 """
        self.ui.textbrow_info.setText(info)
        self.ui.btn_yes.setText(yes_btn)
        if   yes_btn == "确定":
            self.ui.btn_yes.clicked.connect(self.close)
        elif yes_btn == "下载":
            self.ui.btn_yes.clicked.connect(self.downSoft)

    def downSoft(self):
        """ 跳转下载软件 """
        down_tips = F"正在下载最新版~\n请前往下载中心，找到 {SOFT_ZIP} 解压食用"
        self.ui.textbrow_info.setText(down_tips)
        self.ui.btn_yes.clicked.connect(self.close)
        self.ui.btn_yes.clicked.disconnect(self.downSoft)
        self.ui.btn_yes.setText("确定")
        open_new_tab(DOWN_URL)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    dialog = WinUpdateDialog()
    dialog.show()
    sys.exit(app.exec_())
