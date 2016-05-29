# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_servicos_recomendados.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tela_servicos_recomendados(object):
    def setupUi(self, tela_servicos_recomendados):
        tela_servicos_recomendados.setObjectName("tela_servicos_recomendados")
        tela_servicos_recomendados.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tela_servicos_recomendados.sizePolicy().hasHeightForWidth())
        tela_servicos_recomendados.setSizePolicy(sizePolicy)
        tela_servicos_recomendados.setMinimumSize(QtCore.QSize(640, 480))
        tela_servicos_recomendados.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tela_servicos_recomendados.setWindowIcon(icon)
        self.bg_servicos_recomendados = QtWidgets.QLabel(tela_servicos_recomendados)
        self.bg_servicos_recomendados.setGeometry(QtCore.QRect(-1, 0, 640, 480))
        self.bg_servicos_recomendados.setStyleSheet("background-image: url(:/tela_servicos_recomendados/tela_servicos_recomendados.png);")
        self.bg_servicos_recomendados.setText("")
        self.bg_servicos_recomendados.setObjectName("bg_servicos_recomendados")

        self.retranslateUi(tela_servicos_recomendados)
        QtCore.QMetaObject.connectSlotsByName(tela_servicos_recomendados)

    def retranslateUi(self, tela_servicos_recomendados):
        _translate = QtCore.QCoreApplication.translate
        tela_servicos_recomendados.setWindowTitle(_translate("tela_servicos_recomendados", "Integrator"))

import tela_servicos_recomendados_rc
