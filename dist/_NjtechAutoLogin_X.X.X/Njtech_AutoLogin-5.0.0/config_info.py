from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

class Login:
    def __init__(self):
        self.ui = QUiLoader().load('ui/login.ui')
        self.ui.butt_login.clicked.connect(self.reserve_userword)
    
    def reserve_userword(self):
        userword = [0, 0, 0]
        userword[0] = self.ui.ed_user.text()
        userword[1] = self.ui.ed_pwd.text()
        userword[2] = self.ui.channel.currentText()
        with open('build/Auto_login/userword.txt', 'w') as f:
            for line in range(0, len(userword)):
                f.write(userword[line]+'\n')
        self.ui.close()

app = QApplication([])
login = Login()
login.ui.show()
app.exec_()


