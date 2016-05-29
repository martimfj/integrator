# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Inicial(object):
    def setupUi(self, Inicial):
        Inicial.setObjectName("Inicial")
        Inicial.resize(640, 480)
        Inicial.setStyleSheet("")
        self.botao_servicos = QtWidgets.QCommandLinkButton(Inicial)
        self.botao_servicos.setGeometry(QtCore.QRect(186, 111, 270, 135))
        self.botao_servicos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/botaog - 269x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_servicos.setIcon(icon)
        self.botao_servicos.setIconSize(QtCore.QSize(42, 42))
        self.botao_servicos.setObjectName("botao_servicos")
        self.bg_inicial = QtWidgets.QLabel(Inicial)
        self.bg_inicial.setGeometry(QtCore.QRect(-1, -1, 643, 483))
        self.bg_inicial.setStyleSheet("background-image: url(:/tela_principal/background_telainicial.png);")
        self.bg_inicial.setText("")
        self.bg_inicial.setObjectName("bg_inicial")
        self.botao_calendario = QtWidgets.QCommandLinkButton(Inicial)
        self.botao_calendario.setGeometry(QtCore.QRect(187, 261, 270, 135))
        self.botao_calendario.setText("")
        self.botao_calendario.setIcon(icon)
        self.botao_calendario.setIconSize(QtCore.QSize(42, 42))
        self.botao_calendario.setObjectName("botao_calendario")
        self.botao_infos = QtWidgets.QCommandLinkButton(Inicial)
        self.botao_infos.setGeometry(QtCore.QRect(469, 111, 150, 135))
        self.botao_infos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/botaop - 150x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_infos.setIcon(icon1)
        self.botao_infos.setIconSize(QtCore.QSize(42, 42))
        self.botao_infos.setObjectName("botao_infos")
        self.botao_usuarios = QtWidgets.QCommandLinkButton(Inicial)
        self.botao_usuarios.setGeometry(QtCore.QRect(21, 113, 150, 135))
        self.botao_usuarios.setText("")
        self.botao_usuarios.setIcon(icon1)
        self.botao_usuarios.setIconSize(QtCore.QSize(42, 42))
        self.botao_usuarios.setObjectName("botao_usuarios")
        self.botao_editarperfil = QtWidgets.QCommandLinkButton(Inicial)
        self.botao_editarperfil.setGeometry(QtCore.QRect(21, 261, 150, 135))
        self.botao_editarperfil.setText("")
        self.botao_editarperfil.setIcon(icon1)
        self.botao_editarperfil.setIconSize(QtCore.QSize(42, 42))
        self.botao_editarperfil.setObjectName("botao_editarperfil")
        self.bg_inicial.raise_()
        self.botao_servicos.raise_()
        self.botao_calendario.raise_()
        self.botao_infos.raise_()
        self.botao_usuarios.raise_()
        self.botao_editarperfil.raise_()

        self.retranslateUi(Inicial)
        QtCore.QMetaObject.connectSlotsByName(Inicial)

    def retranslateUi(self, Inicial):
        _translate = QtCore.QCoreApplication.translate
        Inicial.setWindowTitle(_translate("Inicial", "Form"))

import tela_principal_rc
