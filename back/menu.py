# import cv2
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt

def menuActions():
    print("teste")

# def closeWindow():
#     formulario.close()
    
# video = cv2.VideoCapture(0)

# while True:
#     conectado, frame = video.read()
#     cv2.imshow('Video', frame)
    
#     if cv2.waitKey(1)==ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()

def updateLabel3(value):
    formulario.label_3.setText(str(str(value)))
    formulario.label_3.setAlignment(Qt.AlignCenter)
    
def updateLabel4(value):
    formulario.label_4.setText(str(str(value)))
    formulario.label_4.setAlignment(Qt.AlignCenter)

app = QtWidgets.QApplication([])
formulario = uic.loadUi("../front/menu.ui")
formulario.label_3.setAlignment(Qt.AlignCenter)
formulario.label_4.setAlignment(Qt.AlignCenter)

# formulario.pushButton.clicked.connect(menuActions)

formulario.show()
formulario.horizontalSlider.valueChanged.connect(updateLabel3)
formulario.horizontalSlider_2.valueChanged.connect(updateLabel4)

# formulario.label_3.refresh()
    

# formulario.pushButton_2.clicked.connect(closeWindow)
app.exec() 