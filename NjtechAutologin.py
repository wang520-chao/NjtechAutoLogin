import sys
from PyQt5.QtWidgets import QApplication
from windo.win_login import WinLogin, WinLoginControl

if __name__ == '__main__':

    app = QApplication(sys.argv)
    WinLoginControl.loginWin = WinLogin()
    WinLoginControl.loginWin.show()
    sys.exit(app.exec_())
