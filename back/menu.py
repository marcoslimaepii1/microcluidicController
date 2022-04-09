from PyQt5 import uic, QtWidgets

def menuActions():
    print("teste")


app = QtWidgets.QApplication([])
formulario = uic.loadUi("./front/menu.ui")
formulario.pushButton.clicked.connect(menuActions)

formulario.show()
app.exec()