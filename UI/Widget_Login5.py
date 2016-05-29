# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

class Ui_Login(QtGui.QWidget):
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Form"))

import tela_login_rc
