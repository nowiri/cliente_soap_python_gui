from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import geocoder
from zeep import Client 
import json
import cv2
import base64
from listar import Ui_Listar

#SOAP WSDL URL
try:
    url = "https://2p.simocapa.com.do/ws/FormWebServices?wsdl"
    client = Client(url)
except Exception as e:
	print(e)

class Ui_MainWindow(object):


    def setupUi(self, MainWindow, loc):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNombre_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre_2.setGeometry(QtCore.QRect(90, 130, 101, 16))
        self.lblNombre_2.setObjectName("lblNombre_2")
        self.cboxSelect_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSelect_2.setGeometry(QtCore.QRect(200, 130, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboxSelect_2.setFont(font)
        self.cboxSelect_2.setObjectName("cboxSelect_2")
        self.cboxSelect_2.addItem("")
        self.cboxSelect_2.addItem("")
        self.cboxSelect_2.addItem("")
        self.cboxSelect_2.addItem("")
        self.cboxSelect_2.addItem("")
        self.cboxSelect_2.addItem("")
        self.lblUbicacion = QtWidgets.QLabel(self.centralwidget)
        self.lblUbicacion.setGeometry(QtCore.QRect(80, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblUbicacion.setFont(font)
        self.lblUbicacion.setObjectName("lblUbicacion")
        self.txtLatitud = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLatitud.setGeometry(QtCore.QRect(260, 60, 113, 20))
        self.txtLatitud.setReadOnly(True)
        self.txtLatitud.setObjectName("txtLatitud")
        self.lblNombre_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre_3.setGeometry(QtCore.QRect(110, 170, 61, 16))
        self.lblNombre_3.setObjectName("lblNombre_3")
        self.lblLongitud = QtWidgets.QLabel(self.centralwidget)
        self.lblLongitud.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.lblLongitud.setObjectName("lblLongitud")
        self.lblApellido = QtWidgets.QLabel(self.centralwidget)
        self.lblApellido.setGeometry(QtCore.QRect(220, 90, 47, 13))
        self.lblApellido.setObjectName("lblApellido")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 260, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(260, 90, 113, 20))
        self.txtApellido.setObjectName("txtApellido")
        self.cboxSelect_3 = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSelect_3.setGeometry(QtCore.QRect(200, 170, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboxSelect_3.setFont(font)
        self.cboxSelect_3.setObjectName("cboxSelect_3")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.cboxSelect_3.addItem("")
        self.lblLatitud = QtWidgets.QLabel(self.centralwidget)
        self.lblLatitud.setGeometry(QtCore.QRect(220, 60, 47, 13))
        self.lblLatitud.setObjectName("lblLatitud")
        self.txtLongitud = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLongitud.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.txtLongitud.setReadOnly(True)
        self.txtLongitud.setObjectName("txtLongitud")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.lblNombre.setObjectName("lblNombre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        self.menuConsultar = QtWidgets.QMenu(self.menubar)
        self.menuConsultar.setObjectName("menuConsultar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFormularios_por_usuario = QtWidgets.QAction(MainWindow)
        self.actionFormularios_por_usuario.setObjectName("actionFormularios_por_usuario")
        self.menuConsultar.addAction(self.actionFormularios_por_usuario)
        self.menubar.addAction(self.menuConsultar.menuAction())

        self.retranslateUi(MainWindow, loc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionFormularios_por_usuario.triggered.connect(self.openListar)
        self.pushButton.clicked.connect(self.foto)
        self.pushButton_2.clicked.connect(self.send)

    def retranslateUi(self, MainWindow, loc):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APISOAP"))
        self.lblNombre_2.setText(_translate("MainWindow", "Nivel Academico"))
        self.cboxSelect_2.setItemText(0, _translate("MainWindow", "<Select>"))
        self.cboxSelect_2.setItemText(1, _translate("MainWindow", "Basico"))
        self.cboxSelect_2.setItemText(2, _translate("MainWindow", "Medio"))
        self.cboxSelect_2.setItemText(3, _translate("MainWindow", "Grado Universitario"))
        self.cboxSelect_2.setItemText(4, _translate("MainWindow", "Postgrado"))
        self.cboxSelect_2.setItemText(5, _translate("MainWindow", "Doctorado"))
        self.lblUbicacion.setText(_translate("MainWindow", "FORMULARIO (API SOAP)"))
        self.lblNombre_3.setText(_translate("MainWindow", "Provincia"))
        self.lblLongitud.setText(_translate("MainWindow", "Longitud"))
        self.lblApellido.setText(_translate("MainWindow", "Apellido"))
        self.pushButton_2.setText(_translate("MainWindow", "ENVIAR"))
        self.cboxSelect_3.setItemText(0, _translate("MainWindow", "<Select>"))
        self.cboxSelect_3.setItemText(1, _translate("MainWindow", "Dajabón"))
        self.cboxSelect_3.setItemText(2, _translate("MainWindow", "Duarte"))
        self.cboxSelect_3.setItemText(3, _translate("MainWindow", "Espaillat"))
        self.cboxSelect_3.setItemText(4, _translate("MainWindow", "Hermanas Mirabal"))
        self.cboxSelect_3.setItemText(5, _translate("MainWindow", "La Vega"))
        self.cboxSelect_3.setItemText(6, _translate("MainWindow", "Maria Trinidad Sánchez"))
        self.cboxSelect_3.setItemText(7, _translate("MainWindow", "Monseñor Nouel"))
        self.cboxSelect_3.setItemText(8, _translate("MainWindow", "Montecristi"))
        self.cboxSelect_3.setItemText(9, _translate("MainWindow", "Puerto Plata"))
        self.cboxSelect_3.setItemText(10, _translate("MainWindow", "Samaná"))
        self.cboxSelect_3.setItemText(11, _translate("MainWindow", "Sánchez Ramírez"))
        self.cboxSelect_3.setItemText(12, _translate("MainWindow", "Santiago"))
        self.cboxSelect_3.setItemText(13, _translate("MainWindow", "Santiago Rodríguez"))
        self.cboxSelect_3.setItemText(14, _translate("MainWindow", "Valverde"))
        self.lblLatitud.setText(_translate("MainWindow", "Latitud"))
        self.pushButton.setText(_translate("MainWindow", "Tomar Foto"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre"))
        self.menuConsultar.setTitle(_translate("MainWindow", "Consultar"))
        self.actionFormularios_por_usuario.setText(_translate("MainWindow", "Formularios por usuario"))
        self.txtLongitud.setText(str(loc[1]))
        self.txtLatitud.setText(str(loc[0]))

    def foto(self):

        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "lastpicture.jpeg"
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))

        cam.release()
        cv2.destroyAllWindows()

    def send(self):

        #BUILD FOTO OBJECT
        try:
            image = open('lastpicture.jpeg', 'rb') #open binary file in read mode
            image_read = image.read()
            encoded = base64.b64encode(image_read).decode("utf-8")
        except Exception as e:
            print(e)
            return

        fotoObject = {
            "nombre": "pictureSOAP",
            "mimeType": "image/jpeg",
            "fotoBase64": encoded
        }

        #BUILD UBICACION OBJECT
        lat = self.txtLatitud.text()
        lng = self.txtLongitud.text()

        ubicacionObject = {
            "longitud": lng,
            "latitud": lat
        }

        #BUILD FORMULARIO OBJECT
        nombre = self.txtNombre.text()
        apellido = self.txtApellido.text()
        sector = str(self.cboxSelect_3.currentText())
        nivelEscolar = str(self.cboxSelect_2.currentText())

        usuario = {
            "username": "admin",
            "password": "admin",
            "nombre": "Administrador",
            "role": "administrador"
        }

        #foto = fotoObject

        if nombre == "" or apellido == "" or sector == "<Select>" or nivelEscolar == "<Select>":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Campo Vacio")
            msg.setInformativeText('Ningun campo puede estar vacio!')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            formularioObject = {
                "nombre": nombre+" "+apellido,
                "sector": sector,
                "nivelEscolar": nivelEscolar,
                "usuario": usuario,
                "foto": fotoObject
            }

            try:

                fotoJSON = json.dumps(fotoObject)
                ubicacionJSON = json.dumps(ubicacionObject)
                formularioJSON = json.dumps(formularioObject)

                client.service.newForm(formularioJSON,ubicacionJSON,fotoJSON)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Formulario enviado")
                msg.setInformativeText('Formulario enviado con exito!')
                msg.setWindowTitle("Exito!")
                msg.exec_()

            except Exception as e:
                print(e)

    def openListar(self):
        self.listarUI = QtWidgets.QMainWindow()
        self.ui = Ui_Listar()
        self.ui.setupListUi(self.listarUI, client)
        self.listarUI.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    myloc = geocoder.ip('me')
    ui.setupUi(MainWindow, myloc.latlng)
    MainWindow.show()
    sys.exit(app.exec_())
