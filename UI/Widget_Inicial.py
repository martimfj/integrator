# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Inicial.ui'
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

class Ui_Inicial(object):
    def setupUi(self, Inicial):
        Inicial.setObjectName(_fromUtf8("Inicial"))
        Inicial.resize(640, 480)
        Inicial.setStyleSheet(_fromUtf8(""))
        self.botao_servicos = QtGui.QCommandLinkButton(Inicial)
        self.botao_servicos.setGeometry(QtCore.QRect(186, 111, 270, 135))
        self.botao_servicos.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Resources/botaog - 269x135.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_servicos.setIcon(icon)
        self.botao_servicos.setIconSize(QtCore.QSize(42, 42))
        self.botao_servicos.setObjectName(_fromUtf8("botao_servicos"))
        self.bg_inicial = QtGui.QLabel(Inicial)
        self.bg_inicial.setGeometry(QtCore.QRect(-1, -1, 643, 483))
        self.bg_inicial.setStyleSheet(_fromUtf8("background-image: url(:/tela_principal/background_telainicial.png);"))
        self.bg_inicial.setText(_fromUtf8(""))
        self.bg_inicial.setObjectName(_fromUtf8("bg_inicial"))
        self.botao_calendario = QtGui.QCommandLinkButton(Inicial)
        self.botao_calendario.setGeometry(QtCore.QRect(187, 261, 270, 135))
        self.botao_calendario.setText(_fromUtf8(""))
        self.botao_calendario.setIcon(icon)
        self.botao_calendario.setIconSize(QtCore.QSize(42, 42))
        self.botao_calendario.setObjectName(_fromUtf8("botao_calendario"))
        self.botao_infos = QtGui.QCommandLinkButton(Inicial)
        self.botao_infos.setGeometry(QtCore.QRect(469, 111, 150, 135))
        self.botao_infos.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Resources/botaop - 150x135.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_infos.setIcon(icon1)
        self.botao_infos.setIconSize(QtCore.QSize(42, 42))
        self.botao_infos.setObjectName(_fromUtf8("botao_infos"))
        self.botao_usuarios = QtGui.QCommandLinkButton(Inicial)
        self.botao_usuarios.setGeometry(QtCore.QRect(21, 113, 150, 135))
        self.botao_usuarios.setText(_fromUtf8(""))
        self.botao_usuarios.setIcon(icon1)
        self.botao_usuarios.setIconSize(QtCore.QSize(42, 42))
        self.botao_usuarios.setObjectName(_fromUtf8("botao_usuarios"))
        self.botao_editarperfil = QtGui.QCommandLinkButton(Inicial)
        self.botao_editarperfil.setGeometry(QtCore.QRect(21, 261, 150, 135))
        self.botao_editarperfil.setText(_fromUtf8(""))
        self.botao_editarperfil.setIcon(icon1)
        self.botao_editarperfil.setIconSize(QtCore.QSize(42, 42))
        self.botao_editarperfil.setObjectName(_fromUtf8("botao_editarperfil"))
        self.bg_inicial.raise_()
        self.botao_servicos.raise_()
        self.botao_calendario.raise_()
        self.botao_infos.raise_()
        self.botao_usuarios.raise_()
        self.botao_editarperfil.raise_()

        self.retranslateUi(Inicial)
        QtCore.QMetaObject.connectSlotsByName(Inicial)

    def retranslateUi(self, Inicial):
        Inicial.setWindowTitle(_translate("Inicial", "Form", None))

import tela_principal_rc
