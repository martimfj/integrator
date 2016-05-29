# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(640, 480)
        Login.setStyleSheet(_fromUtf8(""))
        self.input_user = QtGui.QLineEdit(Login)
        self.input_user.setGeometry(QtCore.QRect(191, 184, 270, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(14)
        self.input_user.setFont(font)
        self.input_user.setMaxLength(15)
        self.input_user.setFrame(False)
        self.input_user.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_user.setObjectName(_fromUtf8("input_user"))
        self.input_password = QtGui.QLineEdit(Login)
        self.input_password.setGeometry(QtCore.QRect(192, 232, 270, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(14)
        self.input_password.setFont(font)
        self.input_password.setMaxLength(15)
        self.input_password.setFrame(False)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.botao_novouser = QtGui.QCommandLinkButton(Login)
        self.botao_novouser.setGeometry(QtCore.QRect(344, 280, 148, 27))
        self.botao_novouser.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Resources/botao_cadastro - 149x24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_novouser.setIcon(icon)
        self.botao_novouser.setIconSize(QtCore.QSize(149, 24))
        self.botao_novouser.setObjectName(_fromUtf8("botao_novouser"))
        self.botao_enviar = QtGui.QCommandLinkButton(Login)
        self.botao_enviar.setGeometry(QtCore.QRect(474, 202, 46, 44))
        self.botao_enviar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Resources/botaoenviar - 42x42.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_enviar.setIcon(icon1)
        self.botao_enviar.setIconSize(QtCore.QSize(42, 42))
        self.botao_enviar.setObjectName(_fromUtf8("botao_enviar"))
        self.botao_esqueci = QtGui.QCommandLinkButton(Login)
        self.botao_esqueci.setGeometry(QtCore.QRect(197, 288, 120, 16))
        self.botao_esqueci.setText(_fromUtf8(""))
        self.botao_esqueci.setIcon(icon)
        self.botao_esqueci.setIconSize(QtCore.QSize(149, 24))
        self.botao_esqueci.setObjectName(_fromUtf8("botao_esqueci"))
        self.bg_login = QtGui.QLabel(Login)
        self.bg_login.setGeometry(QtCore.QRect(-1, -1, 644, 483))
        self.bg_login.setStyleSheet(_fromUtf8("background-image: url(:/tela_login/background_telalogin.png);"))
        self.bg_login.setText(_fromUtf8(""))
        self.bg_login.setObjectName(_fromUtf8("bg_login"))
        self.bg_login.raise_()
        self.input_user.raise_()
        self.input_password.raise_()
        self.botao_novouser.raise_()
        self.botao_enviar.raise_()
        self.botao_esqueci.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Form", None))

import tela_login_rc
