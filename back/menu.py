from PyQt5 import uic, QtWidgets

def menuActions():
    print("teste")

def closeWindow():
    formulario.close()

app = QtWidgets.QApplication([])
formulario = uic.loadUi("../front/menu.ui")
formulario.pushButton.clicked.connect(menuActions)

formulario.show()
formulario.pushButton_2.clicked.connect(closeWindow)
app.exec() 