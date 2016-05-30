# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_servicos.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
import tela_servicos_rc
from Widget_servicos_recomendados import Widget_Servicos_recomendados

class Widget_Servicos(QtGui.QWidget):
    def __init__(self):
        super(Widget_Servicos, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tela_servicos")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.bg_servicos = QtGui.QLabel(self)
        self.bg_servicos.setGeometry(QtCore.QRect(-2, 0, 640, 480))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_servicos.sizePolicy().hasHeightForWidth())
        self.bg_servicos.setSizePolicy(sizePolicy)
        self.bg_servicos.setMinimumSize(QtCore.QSize(640, 480))
        self.bg_servicos.setMaximumSize(QtCore.QSize(640, 480))
        self.bg_servicos.setStyleSheet("background-image: url(:/tela_servicos/tela_servicos.png);")
        self.bg_servicos.setText("")
        self.bg_servicos.setObjectName("bg_servicos")

        self.webview_mapagoogle = QWebView(self)
        self.webview_mapagoogle.setGeometry(QtCore.QRect(10, 12, 616, 406))
        self.webview_mapagoogle.setUrl(QtCore.QUrl("about:blank"))
        self.webview_mapagoogle.setObjectName("webview_mapagoogle")
        self.webview_mapagoogle.load(QUrl("https://www.google.com.br/maps/@-23.5979074,-46.6773694,16.96z"))

        self.botao_voltar_servicos = QtGui.QCommandLinkButton(self)
        self.botao_voltar_servicos.setGeometry(QtCore.QRect(4, 436, 92, 37))
        self.botao_voltar_servicos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_servicos.setIcon(icon1)
        self.botao_voltar_servicos.setObjectName("botao_voltar_servicos")

        self.botao_lugares_reco = QtGui.QCommandLinkButton(self)
        self.botao_lugares_reco.setGeometry(QtCore.QRect(522, 436, 110, 37))
        self.botao_lugares_reco.setText("")
        self.botao_lugares_reco.setIcon(icon1)
        self.botao_lugares_reco.setObjectName("botao_lugares_reco")
        
        self.botao_lugares_reco.clicked.connect(self.recomendadosClicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos", "Integrator"))
        
    def recomendadosClicked(self):
        self.recomendados = Widget_Servicos_recomendados()
        self.recomendados.show()