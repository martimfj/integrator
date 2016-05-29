# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from firebase import firebase 
import bg_rc
import tela_login_rc
import tela_principal_rc

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
                
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-image: url(:/bg/background_principal.png);")
        self.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

###-----------------Código editado---------------###
        self.centralwidget = QtGui.QStackedWidget()
        self.setCentralWidget(self.centralwidget)
        login_widget = LoginWidget(self)
        login_widget.botao_enviar.clicked.connect(self.TrocarTela)
###----------------------------------------------###

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Integrator"))

    def TrocarTela(self):
        menu = Menu_Widget(self)
        self.centralwidget.addWidget(menu)
        self.centralwidget.setCurrentWidget(menu)

class Ui_Login(QtGui.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Login")
        self.resize(640, 480)
        self.setStyleSheet("")
        self.input_user = QtGui.QLineEdit(self)
        self.input_user.setGeometry(QtCore.QRect(191, 184, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_user.setFont(font)
        self.input_user.setMaxLength(15)
        self.input_user.setFrame(False)
        self.input_user.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_user.setObjectName("input_user")
        self.input_password = QtGui.QLineEdit(self)
        self.input_password.setGeometry(QtCore.QRect(192, 232, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_password.setFont(font)
        self.input_password.setMaxLength(15)
        self.input_password.setFrame(False)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.botao_novouser = QtGui.QCommandLinkButton(self)
        self.botao_novouser.setGeometry(QtCore.QRect(344, 280, 148, 27))
        self.botao_novouser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/botao_cadastro - 149x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_novouser.setIcon(icon)
        self.botao_novouser.setIconSize(QtCore.QSize(149, 24))
        self.botao_novouser.setObjectName("botao_novouser")
        self.botao_enviar = QtGui.QCommandLinkButton(self)
        self.botao_enviar.setGeometry(QtCore.QRect(474, 202, 46, 44))
        self.botao_enviar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_enviar.setIcon(icon1)
        self.botao_enviar.setIconSize(QtCore.QSize(42, 42))
        self.botao_enviar.setObjectName("botao_enviar")
        self.botao_esqueci = QtGui.QCommandLinkButton(self)
        self.botao_esqueci.setGeometry(QtCore.QRect(197, 288, 120, 16))
        self.botao_esqueci.setText("")
        self.botao_esqueci.setIcon(icon)
        self.botao_esqueci.setIconSize(QtCore.QSize(149, 24))
        self.botao_esqueci.setObjectName("botao_esqueci")
        self.bg_login = QtGui.QLabel(self)
        self.bg_login.setGeometry(QtCore.QRect(-1, -1, 644, 483))
        self.bg_login.setStyleSheet("background-image: url(:/tela_login/background_telalogin.png);")
        self.bg_login.setText("")
        self.bg_login.setObjectName("bg_login")
        self.bg_login.raise_()
        self.input_user.raise_()
        self.input_password.raise_()
        self.botao_novouser.raise_()
        self.botao_enviar.raise_()
        self.botao_esqueci.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

###-----------------Código editado---------------###
        self.setLayout(Login)
###----------------------------------------------###

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Form"))
