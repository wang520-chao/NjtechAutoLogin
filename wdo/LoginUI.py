# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Aerk\Documents\PrjcDev\NjtechAutoLogin-Dev\NjtechAutoLogin-Win\ui\LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/应用图标/icons/NJtech02.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget{\n"
"  border-radius:8px;\n"
"  background: #FFFFFF;\n"
"}\n"
"QLineEdit{\n"
"  border:1px solid rgb(200, 200, 200);\n"
"  background-color: rgb(245, 245, 245);\n"
"}\n"
"QCheckBox{\n"
"  background: transparent;\n"
"}\n"
"\n"
"\n"
"QToolButton{\n"
"  background: transparent;\n"
"  color: rgba(161, 164, 166, 255);\n"
"}\n"
"QToolButton:hover{\n"
"  background: transparent;\n"
"  color:#5846B0;\n"
"}")
        self.topic = QtWidgets.QLabel(Form)
        self.topic.setGeometry(QtCore.QRect(0, 30, 799, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.topic.setFont(font)
        self.topic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.topic.setAutoFillBackground(False)
        self.topic.setStyleSheet("background: transparent;\n"
"")
        self.topic.setAlignment(QtCore.Qt.AlignCenter)
        self.topic.setObjectName("topic")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 140, 801, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.ed_usr = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ed_usr.sizePolicy().hasHeightForWidth())
        self.ed_usr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ed_usr.setFont(font)
        self.ed_usr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ed_usr.setStyleSheet("")
        self.ed_usr.setText("")
        self.ed_usr.setMaxLength(12)
        self.ed_usr.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_usr.setObjectName("ed_usr")
        self.horizontalLayout_3.addWidget(self.ed_usr)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 20)
        self.horizontalLayout_3.setStretch(1, 25)
        self.horizontalLayout_3.setStretch(2, 20)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 210, 801, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.ed_pwd = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ed_pwd.sizePolicy().hasHeightForWidth())
        self.ed_pwd.setSizePolicy(sizePolicy)
        self.ed_pwd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ed_pwd.setFont(font)
        self.ed_pwd.setStyleSheet("")
        self.ed_pwd.setText("")
        self.ed_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ed_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_pwd.setObjectName("ed_pwd")
        self.horizontalLayout_4.addWidget(self.ed_pwd)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.setStretch(0, 20)
        self.horizontalLayout_4.setStretch(1, 25)
        self.horizontalLayout_4.setStretch(2, 20)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 320, 801, 63))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSpacing(0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cbbx_channel = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbbx_channel.sizePolicy().hasHeightForWidth())
        self.cbbx_channel.setSizePolicy(sizePolicy)
        self.cbbx_channel.setMinimumSize(QtCore.QSize(75, 0))
        self.cbbx_channel.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setKerning(False)
        self.cbbx_channel.setFont(font)
        self.cbbx_channel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.cbbx_channel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbbx_channel.setAutoFillBackground(False)
        self.cbbx_channel.setStyleSheet("QComboBox{\n"
"background: #F5F5F5;\n"
"border:1px solid rgb(200, 200, 200);\n"
"border-radius:4px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"image: url(:/组件元素/components/arrow_down.png);\n"
"width: 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position: top right;\n"
"     width: 15px;\n"
"     border-left: 1px solid darkgray;\n"
"     border-top-right-radius: 4px; \n"
"     border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    background: #F9F9F9;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    outline: 0px;  \n"
"}\n"
"")
        self.cbbx_channel.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.cbbx_channel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbbx_channel.setDuplicatesEnabled(False)
        self.cbbx_channel.setObjectName("cbbx_channel")
        self.cbbx_channel.addItem("")
        self.cbbx_channel.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbbx_channel)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setSpacing(0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spbox_cnct_time = QtWidgets.QSpinBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbox_cnct_time.sizePolicy().hasHeightForWidth())
        self.spbox_cnct_time.setSizePolicy(sizePolicy)
        self.spbox_cnct_time.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.spbox_cnct_time.setFont(font)
        self.spbox_cnct_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spbox_cnct_time.setStyleSheet("QSpinBox {\n"
"background-color: #F5F5F5;\n"
"border:1px solid rgb(200, 200, 200);\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"border-image:url(:/组件元素/components/arrow_up.png);\n"
"margin-right:3px;\n"
"margin-top:1px;\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"QSpinBox::down-button {\n"
"border-image:url(:/组件元素/components/arrow_down.png);\n"
"margin-right:3px;\n"
"margin-top:1px;\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"margin-top:2px;\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom:2px;\n"
"}\n"
"")
        self.spbox_cnct_time.setWrapping(False)
        self.spbox_cnct_time.setFrame(False)
        self.spbox_cnct_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spbox_cnct_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spbox_cnct_time.setSpecialValueText("")
        self.spbox_cnct_time.setAccelerated(False)
        self.spbox_cnct_time.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.spbox_cnct_time.setPrefix("")
        self.spbox_cnct_time.setMinimum(-1)
        self.spbox_cnct_time.setMaximum(6000)
        self.spbox_cnct_time.setSingleStep(60)
        self.spbox_cnct_time.setProperty("value", 5)
        self.spbox_cnct_time.setDisplayIntegerBase(10)
        self.spbox_cnct_time.setObjectName("spbox_cnct_time")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spbox_cnct_time)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ckbx_pwrboot = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckbx_pwrboot.sizePolicy().hasHeightForWidth())
        self.ckbx_pwrboot.setSizePolicy(sizePolicy)
        self.ckbx_pwrboot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setKerning(False)
        self.ckbx_pwrboot.setFont(font)
        self.ckbx_pwrboot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ckbx_pwrboot.setStyleSheet("")
        self.ckbx_pwrboot.setIconSize(QtCore.QSize(32, 32))
        self.ckbx_pwrboot.setChecked(False)
        self.ckbx_pwrboot.setAutoRepeat(False)
        self.ckbx_pwrboot.setAutoExclusive(False)
        self.ckbx_pwrboot.setAutoRepeatInterval(100)
        self.ckbx_pwrboot.setTristate(False)
        self.ckbx_pwrboot.setObjectName("ckbx_pwrboot")
        self.verticalLayout_2.addWidget(self.ckbx_pwrboot)
        self.ckbx_showlogin = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckbx_showlogin.sizePolicy().hasHeightForWidth())
        self.ckbx_showlogin.setSizePolicy(sizePolicy)
        self.ckbx_showlogin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setKerning(False)
        self.ckbx_showlogin.setFont(font)
        self.ckbx_showlogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ckbx_showlogin.setStyleSheet("")
        self.ckbx_showlogin.setIconSize(QtCore.QSize(32, 32))
        self.ckbx_showlogin.setChecked(False)
        self.ckbx_showlogin.setAutoRepeat(False)
        self.ckbx_showlogin.setAutoExclusive(False)
        self.ckbx_showlogin.setTristate(False)
        self.ckbx_showlogin.setObjectName("ckbx_showlogin")
        self.verticalLayout_2.addWidget(self.ckbx_showlogin)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.setStretch(0, 10)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 6)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_7.setStretch(0, 20)
        self.horizontalLayout_7.setStretch(1, 22)
        self.horizontalLayout_7.setStretch(2, 20)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 410, 801, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton{\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:0.871, y2:0.25, stop:0.144279 rgba(102, 176, 240, 255));\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"      color: rgb(255, 255, 255);\n"
"    background-color:rgb(48, 152, 241);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"      color: rgb(255, 255, 255);\n"
"    background-color:rgb(36, 146, 241);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.btn_login.setCheckable(True)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_5.addWidget(self.btn_login)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_5.setStretch(0, 20)
        self.horizontalLayout_5.setStretch(1, 25)
        self.horizontalLayout_5.setStretch(2, 20)
        self.layoutWidget4 = QtWidgets.QWidget(Form)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 510, 801, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_feedback = QtWidgets.QToolButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_feedback.sizePolicy().hasHeightForWidth())
        self.btn_feedback.setSizePolicy(sizePolicy)
        self.btn_feedback.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        self.btn_feedback.setFont(font)
        self.btn_feedback.setStyleSheet("")
        self.btn_feedback.setObjectName("btn_feedback")
        self.horizontalLayout_2.addWidget(self.btn_feedback)
        self.btn_givereward = QtWidgets.QToolButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_givereward.sizePolicy().hasHeightForWidth())
        self.btn_givereward.setSizePolicy(sizePolicy)
        self.btn_givereward.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        self.btn_givereward.setFont(font)
        self.btn_givereward.setStyleSheet("")
        self.btn_givereward.setObjectName("btn_givereward")
        self.horizontalLayout_2.addWidget(self.btn_givereward)
        self.btn_upgrade = QtWidgets.QToolButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upgrade.sizePolicy().hasHeightForWidth())
        self.btn_upgrade.setSizePolicy(sizePolicy)
        self.btn_upgrade.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        self.btn_upgrade.setFont(font)
        self.btn_upgrade.setStyleSheet("")
        self.btn_upgrade.setObjectName("btn_upgrade")
        self.horizontalLayout_2.addWidget(self.btn_upgrade)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_8.setStretch(0, 20)
        self.horizontalLayout_8.setStretch(1, 25)
        self.horizontalLayout_8.setStretch(2, 20)

        self.retranslateUi(Form)
        self.btn_login.clicked['bool'].connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_feedback, self.btn_givereward)
        Form.setTabOrder(self.btn_givereward, self.btn_upgrade)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "南工大自动认证"))
        self.topic.setText(_translate("Form", "上网认证 - 登录配置"))
        self.ed_usr.setPlaceholderText(_translate("Form", " 学号"))
        self.ed_pwd.setPlaceholderText(_translate("Form", " 密码"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">选择校园卡对应的宽带运营商</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "宽带"))
        self.cbbx_channel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">选择校园卡对应的宽带运营商</span></p></body></html>"))
        self.cbbx_channel.setItemText(0, _translate("Form", "中国移动"))
        self.cbbx_channel.setItemText(1, _translate("Form", "中国电信"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">定时自启进程，确保网络畅通，后台占用极小 (间隔时间：秒)。设置为 -1 时，关闭断网重连，不保留后台进程</span></p></body></html>"))
        self.label.setText(_translate("Form", "定时重连"))
        self.spbox_cnct_time.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">定时自启进程，确保网络畅通，后台占用极小 (间隔时间：秒)。设置为 -1 时，关闭断网重连，不保留后台进程</span></p></body></html>"))
        self.spbox_cnct_time.setSuffix(_translate("Form", "s"))
        self.ckbx_pwrboot.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">开机自动认证，在校使用期间务必勾选</span></p></body></html>"))
        self.ckbx_pwrboot.setStatusTip(_translate("Form", "0"))
        self.ckbx_pwrboot.setText(_translate("Form", "开机自动认证"))
        self.ckbx_showlogin.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">自动认证时，调用cmd黑窗，展示认证过程信息</span></p></body></html>"))
        self.ckbx_showlogin.setStatusTip(_translate("Form", "0"))
        self.ckbx_showlogin.setText(_translate("Form", "显示认证过程"))
        self.btn_login.setText(_translate("Form", "保存"))
        self.btn_feedback.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">联系与反馈，使用与说明，新增与功能</span></p></body></html>"))
        self.btn_feedback.setWhatsThis(_translate("Form", "<html><head/><body><p>联系反馈，使用说明，新增功能</p></body></html>"))
        self.btn_feedback.setText(_translate("Form", "反馈说明"))
        self.btn_givereward.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">客官，觉得好用打个赏吧，CSDN关注点赞也可以哟，谢谢嘞</span></p></body></html>"))
        self.btn_givereward.setText(_translate("Form", "打赏点赞"))
        self.btn_upgrade.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt;\">请到我的博客下获取最新版，为了软件的安全可靠</span></p></body></html>"))
        self.btn_upgrade.setText(_translate("Form", "检查更新"))

