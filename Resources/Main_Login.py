# Agredecimentos ao Ivica por compartilhar um jeito de fazer a transição de telas no Stackoverflow
# http://stackoverflow.com/questions/22697901/how-do-i-switch-layouts-in-a-window-using-pyqt-without-closing-opening-window

# Trabalho realizado por Martim José, Matheus Pamplona e Raphael Costa
# Projeto final de Design de Software - Insper

from PyQt4 import QtCore, QtGui
from firebase import firebase 
from ver_perfis import Ui_JanelPerfil
from calendario_e_todo import Ui_Calendario
from Widget_servicos import Widget_Servicos
import tela_login_rc #Arquivo Resource da tela de login convertido em Py
import tela_principal_rc #Arquivo Resource da tela menu convertido em Py
import tela_cadastro_rc

import tela_servicos_rc
import tela_servicos_recomendados_rc
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

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
        self.setMinimumSize(QtCore.QSize(640, 480))
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

        self.botao_enviar.clicked.connect(self.tentativalogin)
        self.botao_novouser.clicked.connect(self.novousuario)

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
                    self.botao_enviar.clicked.connect(self.login)
                else:
                    QtGui.QMessageBox.warning(self, "Erro de validação", "Senha Inválida!")
            except TypeError:
                QtGui.QMessageBox.warning(self, "Erro de validação", "Usuario Inválido")

    def login(self):
        self.Tela_menu = LoggedWidget(self)
        self.setCentralWidget(self.Tela_menu)

    def novousuario(self):
    	self.cadastro = Widget_Cadastro(self)
    	self.setCentralWidget(self.cadastro)

    def voltar_login(self):
        self.setupUi()
        self.setCentralWidget(self.Widget_login)




class LoggedWidget(QtGui.QWidget):
    def __init__(self, logprin):
        super(LoggedWidget, self).__init__()
        self.setupUi()
        self.fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.logprin = logprin
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
        self.botao_servicos.clicked.connect(self.abrir_servicos)
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.botao_usuarios.clicked.connect(self.usuariosClicked)
        self.botao_calendario.clicked.connect(self.calendarioClicked)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Inicial", "Form"))
        
    def usuariosClicked(self):
        self.perfis = Ui_JanelPerfil()
        self.perfis.show()
    def calendarioClicked(self):
        self.calendario = Ui_Calendario(self)
        self.calendario.show()
    def abrir_servicos(self):
        self.servicos = Widget_Servicos()
        self.servicos.show()

class Widget_Cadastro(QtGui.QWidget):
    def __init__(self, parent):
        super(Widget_Cadastro, self).__init__(parent)
        self.setupUi()
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

    def setupUi(self):
        self.setObjectName("Widget_Cadastro")
        self.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/system_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAutoFillBackground(True)
        self.bg_cadastro = QtGui.QLabel(self)
        self.bg_cadastro.setGeometry(QtCore.QRect(0, 0, 640, 486))
        self.bg_cadastro.setStyleSheet("background-image: url(:/bg/tela_cadastro.png);")
        self.bg_cadastro.setText("")
        self.bg_cadastro.setObjectName("bg_cadastro")
        self.Widget_Cadastro = QtGui.QWidget(self)



        self.input_snapchat = QtGui.QLineEdit(self)
        self.input_snapchat.setGeometry(QtCore.QRect(504, 389, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_snapchat.setFont(font)
        self.input_snapchat.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_snapchat.setFrame(False)
        self.input_snapchat.setObjectName("input_snapchat")

        self.input_instagram = QtGui.QLineEdit(self)
        self.input_instagram.setGeometry(QtCore.QRect(324, 389, 124, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_instagram.setFont(font)
        self.input_instagram.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_instagram.setFrame(False)
        self.input_instagram.setObjectName("input_instagram")

        self.input_fb = QtGui.QLineEdit(self)
        self.input_fb.setGeometry(QtCore.QRect(50, 389, 216, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_fb.setFont(font)
        self.input_fb.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_fb.setFrame(False)
        self.input_fb.setObjectName("input_fb")

        self.combo_curso = QtGui.QComboBox(self)
        self.combo_curso.setGeometry(QtCore.QRect(68, 182, 352, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.combo_curso.setFont(font)
        self.combo_curso.setObjectName("combo_curso")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/icones_cursos/adm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Resources/icones_cursos/eco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Resources/icones_cursos/computacao.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Resources/icones_cursos/plainicon.com-45939-512px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Resources/icones_cursos/meca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo_curso.addItem(icon5, "")

        self.combo_semestre = QtGui.QComboBox(self)
        self.combo_semestre.setGeometry(QtCore.QRect(521, 182, 104, 22))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.combo_semestre.setFont(font)
        self.combo_semestre.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combo_semestre.setFrame(True)
        self.combo_semestre.setObjectName("combo_semestre")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")
        self.combo_semestre.addItem("")

        self.input_nome = QtGui.QLineEdit(self)
        self.input_nome.setGeometry(QtCore.QRect(75, 40, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_nome.setFont(font)
        self.input_nome.setFrame(False)
        self.input_nome.setEchoMode(QtGui.QLineEdit.Normal)
        self.input_nome.setObjectName("input_nome")
        # self.input_nome.setValidator(self.validator_nome)
        # self.input_nome.textChanged.connect(self.check_state_nome)
        reg_exp = QtCore.QRegExp("[^0-9\.\,\"\?\!\;\:\#\$\%\&\(\)\*\+\-\/\<\>\=\@\[\]\\\^\_\{\}\|\~]+")
        textvalidator = QtGui.QRegExpValidator(reg_exp, self.input_nome)
        self.input_nome.setValidator(textvalidator)
        self.input_nome.setPlaceholderText("Digite seu nome completo")


        self.input_nasci = QtGui.QDateEdit(self)
        self.input_nasci.setGeometry(QtCore.QRect(548, 40, 78, 22))
        self.input_nasci.setFrame(False)
        self.input_nasci.setReadOnly(False)
        self.input_nasci.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.input_nasci.setDate(QtCore.QDate(1997, 1, 1))
        self.input_nasci.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(23, 59, 59)))
        self.input_nasci.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 9, 14), QtCore.QTime(0, 0, 0)))
        self.input_nasci.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.input_nasci.setCalendarPopup(False)
        self.input_nasci.setObjectName("input_nasci")

        self.input_newuser = QtGui.QLineEdit(self)
        self.input_newuser.setGeometry(QtCore.QRect(82, 87, 116, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newuser.setFont(font)
        self.input_newuser.setFrame(False)
        self.input_newuser.setObjectName("input_newuser")
        reg_exp_user = QtCore.QRegExp("[a-z]+")
        uservalidator = QtGui.QRegExpValidator(reg_exp_user, self.input_newuser)
        self.input_newuser.setValidator(uservalidator)
        # self.input_newuser.setValidator(self.validator_usuario)
        # self.input_newuser.textChanged.connect(self.check_state_usuario)
        self.input_newuser.setPlaceholderText("a-z")

        self.input_newpw = QtGui.QLineEdit(self)
        self.input_newpw.setGeometry(QtCore.QRect(270, 87, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newpw.setFont(font)
        self.input_newpw.setText("")
        self.input_newpw.setMaxLength(15)
        self.input_newpw.setFrame(False)
        self.input_newpw.setEchoMode(QtGui.QLineEdit.Password)
        self.input_newpw.setObjectName("input_newpw")
        reg_exp_pw = QtCore.QRegExp("\w+")
        pwvalidator = QtGui.QRegExpValidator(reg_exp_pw, self.input_newpw)
        self.input_newpw.setValidator(pwvalidator)
        # self.input_newpw.setValidator(self.validator_senha)
        # self.input_newpw.textChanged.connect(self.check_state_senha)
        self.input_newpw.setPlaceholderText("a-z e 0-9")

        self.input_newpw_conf = QtGui.QLineEdit(self)
        self.input_newpw_conf.setGeometry(QtCore.QRect(521, 87, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_newpw_conf.setFont(font)
        self.input_newpw_conf.setText("")
        self.input_newpw_conf.setMaxLength(15)
        self.input_newpw_conf.setFrame(False)
        self.input_newpw_conf.setEchoMode(QtGui.QLineEdit.Password)
        self.input_newpw_conf.setObjectName("input_newpw_conf")
        pwvalidator = QtGui.QRegExpValidator(reg_exp_pw, self.input_newpw_conf)
        self.input_newpw_conf.setValidator(pwvalidator)
        # self.input_newpw_conf.setValidator(self.validator_confsenha)
        # self.input_newpw_conf.textChanged.connect(self.check_state_senha)
        self.input_newpw_conf.setPlaceholderText("a-z e 0-9")

        self.input_email = QtGui.QLineEdit(self)
        self.input_email.setGeometry(QtCore.QRect(63, 353, 314, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_email.setFont(font)
        self.input_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_email.setFrame(False)
        self.input_email.setObjectName("input_email")
        reg_exp_email = QtCore.QRegExp("^([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}$")
        emailvalidator = QtGui.QRegExpValidator(reg_exp_email, self.input_email)
        self.input_email.setValidator(emailvalidator)
        self.input_email.setPlaceholderText("fulano@al.insper.edu.br")

        self.input_telefone = QtGui.QLineEdit(self)
        self.input_telefone.setGeometry(QtCore.QRect(471, 353, 152, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.input_telefone.setFont(font)
        self.input_telefone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_telefone.setFrame(False)
        self.input_telefone.setObjectName("input_telefone")
        reg_exp_telef = QtCore.QRegExp("(?:^\([0]?[1-9]{2}\)|^[0]?[1-9]{2}[\.-\s]?)[9]?[1-9]\d{3}[\.-\s]?\d{4}$")
        telvalidator = QtGui.QRegExpValidator(reg_exp_telef, self.input_telefone)
        self.input_telefone.setValidator(telvalidator)
        self.input_telefone.setPlaceholderText("Ex: (11)92222-3333")

        self.check_atletica = QtGui.QCheckBox(self)
        self.check_atletica.setGeometry(QtCore.QRect(20, 238, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_atletica.setFont(font)
        self.check_atletica.setObjectName("check_atletica")

        self.check_aisec = QtGui.QCheckBox(self)
        self.check_aisec.setGeometry(QtCore.QRect(20, 258, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_aisec.setFont(font)
        self.check_aisec.setObjectName("check_aisec")
        self.check_bateria = QtGui.QCheckBox(self)
        self.check_bateria.setGeometry(QtCore.QRect(20, 278, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_bateria.setFont(font)
        self.check_bateria.setObjectName("check_bateria")
        self.check_bemgasto = QtGui.QCheckBox(self)
        self.check_bemgasto.setGeometry(QtCore.QRect(20, 298, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_bemgasto.setFont(font)
        self.check_bemgasto.setObjectName("check_bemgasto")
        self.check_designchallenge = QtGui.QCheckBox(self)
        self.check_designchallenge.setGeometry(QtCore.QRect(190, 258, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_designchallenge.setFont(font)
        self.check_designchallenge.setObjectName("check_designchallenge")
        self.check_da = QtGui.QCheckBox(self)
        self.check_da.setGeometry(QtCore.QRect(190, 278, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_da.setFont(font)
        self.check_da.setObjectName("check_da")
        self.check_infinance = QtGui.QCheckBox(self)
        self.check_infinance.setGeometry(QtCore.QRect(390, 238, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_infinance.setFont(font)
        self.check_infinance.setObjectName("check_infinance")
        self.check_junior = QtGui.QCheckBox(self)
        self.check_junior.setGeometry(QtCore.QRect(390, 258, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_junior.setFont(font)
        self.check_junior.setObjectName("check_junior")
        self.check_post = QtGui.QCheckBox(self)
        self.check_post.setGeometry(QtCore.QRect(390, 278, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_post.setFont(font)
        self.check_post.setObjectName("check_post")
        self.check_ligaemp = QtGui.QCheckBox(self)
        self.check_ligaemp.setGeometry(QtCore.QRect(390, 298, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_ligaemp.setFont(font)
        self.check_ligaemp.setObjectName("check_ligaemp")
        self.check_consilium = QtGui.QCheckBox(self)
        self.check_consilium.setGeometry(QtCore.QRect(190, 238, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_consilium.setFont(font)
        self.check_consilium.setObjectName("check_consilium")
        self.check_enactus = QtGui.QCheckBox(self)
        self.check_enactus.setGeometry(QtCore.QRect(190, 298, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_enactus.setFont(font)
        self.check_enactus.setObjectName("check_enactus")
        self.check_gas = QtGui.QCheckBox(self)
        self.check_gas.setGeometry(QtCore.QRect(190, 318, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_gas.setFont(font)
        self.check_gas.setObjectName("check_gas")
        self.check_sementes = QtGui.QCheckBox(self)
        self.check_sementes.setGeometry(QtCore.QRect(390, 318, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.check_sementes.setFont(font)
        self.check_sementes.setObjectName("check_sementes")

        self.botao_fb = QtGui.QCommandLinkButton(self)
        self.botao_fb.setGeometry(QtCore.QRect(11, 384, 27, 27))
        self.botao_fb.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Resources/botaoenviar - 42x42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_fb.setIcon(icon6)
        self.botao_fb.setIconSize(QtCore.QSize(27, 27))
        self.botao_fb.setObjectName("botao_fb")
        import webbrowser
        self.botao_fb.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/profile.php'))

        self.botao_cadastrar = QtGui.QCommandLinkButton(self)
        self.botao_cadastrar.setEnabled(True)
        self.botao_cadastrar.setGeometry(QtCore.QRect(564, 412, 66, 65))
        self.botao_cadastrar.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Resources/botao_cadastrar_act.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("../Resources/botao_cadastrar_inac.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)

        self.botao_cadastrar.setIcon(icon7)
        self.botao_cadastrar.setIconSize(QtCore.QSize(50, 50))
        self.botao_cadastrar.setDescription("")
        self.botao_cadastrar.setObjectName("botao_cadastrar")
        self.botao_cadastrar.clicked.connect(self.ConfirmaSenha)

        self.botao_voltar = QtGui.QCommandLinkButton(self)
        self.botao_voltar.setGeometry(QtCore.QRect(7, 437, 91, 36))
        self.botao_voltar.setText("")
        self.botao_voltar.setIcon(icon6)
        self.botao_voltar.setIconSize(QtCore.QSize(27, 27))
        self.botao_voltar.setObjectName("botao_voltar")
        self.botao_voltar.clicked.connect(self.parent().voltar_login)

        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setTabOrder(self.input_nome, self.input_nasci)
        self.setTabOrder(self.input_nasci, self.input_newuser)
        self.setTabOrder(self.input_newuser, self.input_newpw)
        self.setTabOrder(self.input_newpw, self.input_newpw_conf)
        self.setTabOrder(self.input_newpw_conf, self.combo_curso)
        self.setTabOrder(self.combo_curso, self.combo_semestre)
        self.setTabOrder(self.combo_semestre, self.check_atletica)
        self.setTabOrder(self.check_atletica, self.check_aisec)
        self.setTabOrder(self.check_aisec, self.check_bateria)
        self.setTabOrder(self.check_bateria, self.check_bemgasto)
        self.setTabOrder(self.check_bemgasto, self.check_consilium)
        self.setTabOrder(self.check_consilium, self.check_designchallenge)
        self.setTabOrder(self.check_designchallenge, self.check_da)
        self.setTabOrder(self.check_da, self.check_enactus)
        self.setTabOrder(self.check_enactus, self.check_gas)
        self.setTabOrder(self.check_gas, self.check_infinance)
        self.setTabOrder(self.check_infinance, self.check_junior)
        self.setTabOrder(self.botao_fb, self.check_post)
        self.setTabOrder(self.check_post, self.check_ligaemp)
        self.setTabOrder(self.check_ligaemp, self.check_sementes)
        self.setTabOrder(self.check_sementes, self.input_email)
        self.setTabOrder(self.input_email, self.input_telefone)
        self.setTabOrder(self.input_telefone, self.input_fb)
        self.setTabOrder(self.check_junior, self.botao_fb)
        self.setTabOrder(self.input_fb, self.input_instagram)
        self.setTabOrder(self.input_instagram, self.input_snapchat)
        self.setTabOrder(self.input_snapchat, self.botao_voltar)
        self.setTabOrder(self.botao_voltar, self.botao_cadastrar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Widget_Cadastro", "Cadastro"))
        self.combo_curso.setItemText(0, _translate("Widget_Cadastro", "Administração"))
        self.combo_curso.setItemText(1, _translate("Widget_Cadastro", "Economia"))
        self.combo_curso.setItemText(2, _translate("Widget_Cadastro", "Engenharia da Computação"))
        self.combo_curso.setItemText(3, _translate("Widget_Cadastro", "Engenharia Mecânica"))
        self.combo_curso.setItemText(4, _translate("Widget_Cadastro", "Engenharia Mecatrônica"))
        self.combo_semestre.setItemText(0, _translate("Widget_Cadastro", "1"))
        self.combo_semestre.setItemText(1, _translate("Widget_Cadastro", "2"))
        self.combo_semestre.setItemText(2, _translate("Widget_Cadastro", "3"))
        self.combo_semestre.setItemText(3, _translate("Widget_Cadastro", "4"))
        self.combo_semestre.setItemText(4, _translate("Widget_Cadastro", "5"))
        self.combo_semestre.setItemText(5, _translate("Widget_Cadastro", "6"))
        self.combo_semestre.setItemText(6, _translate("Widget_Cadastro", "7"))
        self.combo_semestre.setItemText(7, _translate("Widget_Cadastro", "8"))
        self.combo_semestre.setItemText(8, _translate("Widget_Cadastro", "9"))
        self.combo_semestre.setItemText(9, _translate("Widget_Cadastro", "10"))
        self.check_atletica.setText(_translate("Widget_Cadastro", "Atlética Insper"))
        self.check_aisec.setText(_translate("Widget_Cadastro", "AISEC"))
        self.check_bateria.setText(_translate("Widget_Cadastro", "Bateria Imperial"))
        self.check_bemgasto.setText(_translate("Widget_Cadastro", "Bem gasto"))
        self.check_designchallenge.setText(_translate("Widget_Cadastro", "Design Challenge"))
        self.check_da.setText(_translate("Widget_Cadastro", "Diretório Acadêmico"))
        self.check_infinance.setText(_translate("Widget_Cadastro", "Infinance"))
        self.check_junior.setText(_translate("Widget_Cadastro", "Insper Junior"))
        self.check_post.setText(_translate("Widget_Cadastro", "Insper Post"))
        self.check_ligaemp.setText(_translate("Widget_Cadastro", "Liga de Empreendedores"))
        self.check_consilium.setText(_translate("Widget_Cadastro", "Consilium Insper"))
        self.check_enactus.setText(_translate("Widget_Cadastro", "Enactus"))
        self.check_gas.setText(_translate("Widget_Cadastro", "Grupo de Ação Social"))
        self.check_sementes.setText(_translate("Widget_Cadastro", "Sementes Culturais"))

    def newuser(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        self.nome = self.input_nome.text()
        self.data = self.input_nasci.text()
        self.usuario = self.input_newuser.text()
        self.novasenha = self.input_newpw.text()
        self.confnovasenha = self.input_newpw_conf.text()

        self.curso = self.combo_curso.currentText()
        self.semestre = self.combo_semestre.currentText()
        self.email = self.input_email.text()
        self.telefone = self.input_telefone.text()
        self.faceb = self.input_fb.text()
        self.insta = self.input_instagram.text()
        self.snap = self.input_snapchat.text()

        user_count = fb.get("/userCount", "/count")
        user_count += 1
        fb.put("/userCount",name = "count", data = user_count)

        fb.put("/users/", name = self.usuario, data = {'name' : self.usuario, 'password' : self.novasenha, 'nome': self.nome, 'aniversario': self.data, 'email' : self.email, 'telefone' : self.telefone,
        'facebook': self.faceb, 'snapchat': self.snap, 'instagram': self.insta, 'entidade': "-", 'semestre': self.semestre, 'curso': self.curso})

        self.checkButtons

    def checkButtons(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")

        if self.check_aisec.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades", data = self.check_aisec.text())
        if self.check_atletica.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades1", data = self.check_atletica.text())
        if self.check_bemgasto.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades2", data = self.check_bemgasto.text())           
        if self.check_bateria.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades3", data = self.check_bateria.text())
        if self.check_consilium.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades4", data = self.check_consilium.text())
        if self.check_da.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades5", data = self.check_da.text())            
        if self.check_designchallenge.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades6", data = self.check_designchallenge.text())           
        if self.check_enactus.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades7", data = self.check_enactus.text())           
        if self.check_infinance.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades8", data = self.check_infinance.text())
        if self.check_gas.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades9", data = self.check_gas.text())
        if self.check_junior.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades10", data = self.check_junior.text())            
        if self.check_post.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades11", data = self.check_post.text())           
        if self.check_ligaemp.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades12", data = self.check_ligaemp.text())
        if self.check_sementes.isChecked():
            fb.put("/users/{0}/entidade".format(self.usuario), name = "entidades13", data = self.check_sementes.text())    
        
        QtGui.QMessageBox.warning(self, "Confirmação", "Usuário Cadastrado")    
        self.parent().voltar_login()

    def ConfirmaSenha(self):
        fb = firebase.FirebaseApplication("https://dsoftintegrator.firebaseio.com/")
        
        
        self.nome = self.input_nome.text()
        self.data = self.input_nasci.text()
        self.usuario = self.input_newuser.text()
        self.novasenha = self.input_newpw.text()
        self.confnovasenha = self.input_newpw_conf.text()
        
        usuarios_existentes = []
        dicionario = fb.get("/users", None)
        for usuario in dicionario:
            usuarios_existentes.append(usuario)

        for usuario in usuarios_existentes:
            if self.usuario == usuario:
                QtGui.QMessageBox.warning(self, "Erro na confirmação", "Usuario já existente")
        
        if self.novasenha == self.confnovasenha:
            self.newuser()
            self.checkButtons()
        else:
            QtGui.QMessageBox.warning(self, "Erro na confirmação", "As senhas não coincidem")
        

#fazer a qline edit mudar de cor conforme o texto ta certo ou errado
#preencha os campos mínimos por favor
#esqueci a senha, manda email para a pessoa
#linkar a aba editar perfil com o menu



if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
