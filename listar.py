
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import json
from texttable import *


class Ui_Listar(object):
    def setupListUi(self, MainWindow, client):
        MainWindow.setObjectName("MainWindow")

        #GETTIN WSDL REFERENCE
        self.client = client;

        MainWindow.resize(600, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.txtUsuario.setObjectName("txtUsuario")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(90, 20, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.btnConsultar.setObjectName("btnConsultar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 60, 580, 171))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnConsultar.clicked.connect(self.consultar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consulta"))
        self.lblUsuario.setText(_translate("MainWindow", "Usuario:"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))

        self.plainTextEdit.setPlainText("+----+-------------------+-----------+---------------------+---------+\n"+
                                        "| ID |      NOMBRE       | PROVINCIA |     NIVEL ACAD.     | USUARIO |\n"+
                                        "+====+===================+===========+=====================+=========+\n")


    def consultar(self):
        user = self.txtUsuario.text()

        if user == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Campo Vacio")
            msg.setInformativeText('Favor digite un usuario!')
            msg.setWindowTitle("Error")
            msg.exec_()

            self.plainTextEdit.setPlainText("+----+-------------------+-----------+---------------------+---------+\n"+
                                            "| ID |      NOMBRE       | PROVINCIA |     NIVEL ACAD.     | USUARIO |\n"+
                                            "+====+===================+===========+=====================+=========+\n")

        else:

            try:

                formulariosJSON = self.client.service.listarForms(user);
                formularios = json.loads(formulariosJSON);
                if len(formularios) == 0:
                    self.plainTextEdit.setPlainText("+----+-------------------+-----------+---------------------+---------+\n"+
                                                    "| ID |      NOMBRE       | PROVINCIA |     NIVEL ACAD.     | USUARIO |\n"+
                                                    "+====+===================+===========+=====================+=========+\n")

                else:
                    table = Texttable()
                    table.set_cols_align(["c", "c", "c", "c", "c"])
                    table.set_cols_valign(["m", "m", "m", "m", "m"])
                    table.header(["ID", "NOMBRE", "PROVINCIA", "NIVEL ACAD.", "USUARIO"])

                    for i in range(len(formularios)):

                        table.add_row([formularios[i]["formulario"]["id"],
                                     formularios[i]["formulario"]["nombre"], 
                                     formularios[i]["formulario"]["sector"],
                                     formularios[i]["formulario"]["nivelEscolar"],
                                     formularios[i]["formulario"]["usuario"]["username"]])

                    self.plainTextEdit.setPlainText(table.draw())

            except Exception as e:
                print(e)
                self.plainTextEdit.setPlainText("+----+-------------------+-----------+---------------------+---------+\n"+
                                                "| ID |      NOMBRE       | PROVINCIA |     NIVEL ACAD.     | USUARIO |\n"+
                                                "+====+===================+===========+=====================+=========+\n")
