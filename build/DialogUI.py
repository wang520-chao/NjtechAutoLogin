# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\#HerK\Documents\AllCode\PrjctDev\Njtech-AutoLogin\ui\DialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(748, 321)
        Dialog.setMinimumSize(QtCore.QSize(600, 220))
        Dialog.setStyleSheet("QDialog{\n"
"  border-radius:8px;\n"
"  background: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:0.871, y2:0.25, stop:0.144279 rgba(102, 176, 240, 255));\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius:8px;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    background: transparent;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(590, 10, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        self.pushButton.clicked['bool'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "确定"))