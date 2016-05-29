# Agredecimentos ao Ivica por compartilhar um jeito de fazer a transição de telas no Stackoverflow
# http://stackoverflow.com/questions/22697901/how-do-i-switch-layouts-in-a-window-using-pyqt-without-closing-opening-window

# Trabalho realizado por Martim José, Matheus Pamplona e Raphael Costa
# Projeto final de Design de Software - Insper

from PyQt4 import QtCore, QtGui
from firebase import firebase 
import tela_login_rc #Arquivo Resource da tela de login convertido em Py
import tela_principal_rc #Arquivo Resource da tela menu convertido em Py

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
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
        self.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.Widget_login = QtGui.QWidget(self)
        self.Widget_login.setObjectName("Widget_login")
        self.botao_enviar = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_enviar.setGeometry(QtCore.QRect(474, 203, 46, 44))
        self.botao_enviar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_enviar.setIcon(icon1)
        self.botao_enviar.setIconSize(QtCore.QSize(42, 42))
        self.botao_enviar.setObjectName("botao_enviar")
        self.input_password = QtGui.QLineEdit(self.Widget_login)
        self.input_password.setGeometry(QtCore.QRect(192, 233, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_password.setFont(font)
        self.input_password.setMaxLength(15)
        self.input_password.setFrame(False)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.input_user = QtGui.QLineEdit(self.Widget_login)
        self.input_user.setGeometry(QtCore.QRect(191, 185, 270, 32))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(14)
        self.input_user.setFont(font)
        self.input_user.setMaxLength(15)
        self.input_user.setFrame(False)
        self.input_user.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_user.setObjectName("input_user")
        self.botao_esqueci = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_esqueci.setGeometry(QtCore.QRect(197, 289, 120, 16))
        self.botao_esqueci.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Resources/botao_cadastro - 149x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_esqueci.setIcon(icon2)
        self.botao_esqueci.setIconSize(QtCore.QSize(149, 24))
        self.botao_esqueci.setObjectName("botao_esqueci")
        self.botao_novouser = QtGui.QCommandLinkButton(self.Widget_login)
        self.botao_novouser.setGeometry(QtCore.QRect(344, 281, 148, 27))
        self.botao_novouser.setText("")
        self.botao_novouser.setIcon(icon2)
        self.botao_novouser.setIconSize(QtCore.QSize(149, 24))
        self.botao_novouser.setObjectName("botao_novouser")
        self.bg_login = QtGui.QLabel(self.Widget_login)
        self.bg_login.setGeometry(QtCore.QRect(0, 0, 644, 483))
        self.bg_login.setStyleSheet("background-image: url(:/tela_login/background_telalogin.png);")
        self.bg_login.setText("")
        self.bg_login.setObjectName("bg_login")
        self.bg_login.raise_()
        self.input_user.raise_()
        self.input_password.raise_()
        self.botao_novouser.raise_()
        self.botao_esqueci.raise_()
        self.botao_enviar.raise_()

        self.setCentralWidget(self.Widget_login)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.input_user, self.input_password) #Ordem do TAB -> Login, Senha, Enviar, Novo Usuário, Esqueci Minha senha
        self.setTabOrder(self.input_password, self.botao_enviar)
        self.setTabOrder(self.botao_enviar, self.botao_novouser)
        self.setTabOrder(self.botao_novouser, self.botao_esqueci)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Integrator"))

    def tentativalogin (self):
        # fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

        # usuarios = fb.get('/users', None)
        # self.user = self.input_user.text()
        # self.password = str(self.input_password.text())

        # # if not self.user or self.password:
        # #     QtGui.QMessageBox.warning(self, 'Erro de validação', 'Usuário e senha faltando')

        # # if not self.password:
        # #     QtGui.QMessageBox.warning(self, 'Erro de validação', 'Senha faltando')

        # if self.user in usuarios:
        #     self.dicionario = self.fb.get("/users", "/{0}".format(self.user))
        #     if self.password == self.dicionario["password"]:
        #         Main = MainWindow(self)
        #         logged_in_widget = LoggedWidget(self)
        #         Main.central_widget.addWidget(logged_in_widget)
        #         Main.central_widget.setCurrentWidget(logged_in_widget)
        #         # self.botao_enviar.clicked.connect(Main.login)
        #     else:
        #         QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
        # else:
        #     QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")

        self.user = self.input_user.text()
        self.password = str(self.input_password.text())
        self.dicionario = self.fb.get("/users", "/{0}".format(self.user))
        if not self.user:
            QtGui.QMessageBox.warning(self, 'Erro de validação', 'Usuário faltando')
        elif not self.password:
            QtGui.QMessageBox.warning(self, 'Erro de validação', 'Senha faltando')
        else:  
            try:  
                if self.user == self.dicionario["name"] and self.password == self.dicionario["password"]:
                    Main = MainWindow(self)
                    self.botao_enviar.clicked.connect(login())
                else:
                    QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
            except TypeError:
                QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")

    def login(self):
        Tela_menu = LoggedWidget(self)
        self.central_widget.addWidget(Tela_menu)
        self.central_widget.setCurrentWidget(Tela_menu)

class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Inicial")
        self.resize(640, 480)
        self.setStyleSheet("")
        self.botao_servicos = QtGui.QCommandLinkButton(self)
        self.botao_servicos.setGeometry(QtCore.QRect(186, 111, 270, 135))
        self.botao_servicos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/botaog - 269x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_servicos.setIcon(icon)
        self.botao_servicos.setIconSize(QtCore.QSize(42, 42))
        self.botao_servicos.setObjectName("botao_servicos")
        self.bg_inicial = QtGui.QLabel(self)
        self.bg_inicial.setGeometry(QtCore.QRect(-1, -1, 643, 483))
        self.bg_inicial.setStyleSheet("background-image: url(:/tela_principal/background_telainicial.png);")
        self.bg_inicial.setText("")
        self.bg_inicial.setObjectName("bg_inicial")
        self.botao_calendario = QtGui.QCommandLinkButton(self)
        self.botao_calendario.setGeometry(QtCore.QRect(187, 261, 270, 135))
        self.botao_calendario.setText("")
        self.botao_calendario.setIcon(icon)
        self.botao_calendario.setIconSize(QtCore.QSize(42, 42))
        self.botao_calendario.setObjectName("botao_calendario")
        self.botao_infos = QtGui.QCommandLinkButton(self)
        self.botao_infos.setGeometry(QtCore.QRect(469, 111, 150, 135))
        self.botao_infos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/botaop - 150x135.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_infos.setIcon(icon1)
        self.botao_infos.setIconSize(QtCore.QSize(42, 42))
        self.botao_infos.setObjectName("botao_infos")
        self.botao_usuarios = QtGui.QCommandLinkButton(self)
        self.botao_usuarios.setGeometry(QtCore.QRect(21, 113, 150, 135))
        self.botao_usuarios.setText("")
        self.botao_usuarios.setIcon(icon1)
        self.botao_usuarios.setIconSize(QtCore.QSize(42, 42))
        self.botao_usuarios.setObjectName("botao_usuarios")
        self.botao_editarperfil = QtGui.QCommandLinkButton(self)
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Inicial", "Form"))


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
