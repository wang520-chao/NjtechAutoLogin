from window.win_login import WinLogin, WinLoginControl
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    WinLoginControl.loginWin = WinLogin()
    WinLoginControl.loginWin.show()
    sys.exit(app.exec_())


