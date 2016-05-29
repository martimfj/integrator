from PyQt4 import QtCore, QtGui
import tela_servicos_recomendados_rc

class Widget_Servicos_recomendados(QtGui.QWidget):
    def __init__ (self):
        super(Widget_Servicos_recomendados, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tela_servicos_recomendados")
        self.resize(640, 480)
        self.move(300, 300)
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
        self.bg_servicos_recomendados = QtGui.QLabel(self)
        self.bg_servicos_recomendados.setGeometry(QtCore.QRect(-1, 0, 640, 480))
        self.bg_servicos_recomendados.setStyleSheet("background-image: url(:/tela_servicos_recomendados/tela_servicos_recomendados.png);")
        self.bg_servicos_recomendados.setText("")
        self.bg_servicos_recomendados.setObjectName("bg_servicos_recomendados")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tela_servicos_recomendados", "Integrator"))


