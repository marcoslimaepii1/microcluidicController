import cv2
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# from ui_main_window import *
def controlImage():
        cap = cv2.VideoCapture(2)
        viewCam(cap)
            

def viewCam(cap):
        # read image in BGR format
        ret, image = cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        formulario.image_label.setPixmap(QPixmap.fromImage(qImg))

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

formulario.show()
formulario.horizontalSlider.valueChanged.connect(updateLabel3)
formulario.horizontalSlider_2.valueChanged.connect(updateLabel4)


# timer.timeout.connect(viewCam(cap))
formulario.control_bt.clicked.connect(controlImage)


# formulario.pushButton_2.clicked.connect(closeWindow)
app.exec() 