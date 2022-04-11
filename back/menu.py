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
    if not timer.isActive():
        # create video capture
        cap = cv2.VideoCapture(0)
        # start timer
        timer.start(20)
        # update control_bt text
        formulario.control_bt.setText("Stop")
        viewCam()
    # if timer is started
    else:
        # stop timer
        timer.stop()
        # release video capture
        # cap.release()
        # update control_bt text
        formulario.control_bt.setText("Capture")

def viewCam():
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
    
    if vlib == False and formulario.checkBox.isChecked():
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        my_pwm.setup(11, GPIO.OUT)
        my_pwm = GPIO.PWM(11,10)
        my_pwm.start(50)
     
    if formulario.radioButton.isChecked():
       formulario.horizontalSlider.setMinimum(1)
       formulario.horizontalSlider.setMaximum(192000)
       if formulario.checkBox.isChecked():
            my_pwm.ChangeFrequency(value)

    elif formulario.radioButton_2.isChecked():   
       formulario.horizontalSlider.setMinimum(1)
       formulario.horizontalSlider.setMaximum(19)
       if formulario.checkBox.isChecked():
          my_pwm.ChangeFrequency(value * 1000000)
 
    else:
       formulario.horizontalSlider.setMinimum(1)
       formulario.horizontalSlider.setMaximum(1) 
           
    formulario.label_3.setText(str(str(value)))
    
    formulario.label_3.setAlignment(Qt.AlignCenter)
    
def updateLabel4(value):
    formulario.label_4.setText(str(str(value)))
    formulario.label_4.setAlignment(Qt.AlignCenter)

app = QtWidgets.QApplication([])
formulario = uic.loadUi("../front/menu.ui")
formulario.label_3.setAlignment(Qt.AlignCenter)

vlib = False

formulario.show()
formulario.horizontalSlider.valueChanged.connect(updateLabel3)


timer = QTimer()
timer.timeout.connect(viewCam)
cap = cv2.VideoCapture(0)
formulario.control_bt.clicked.connect(controlImage)


# formulario.pushButton_2.clicked.connect(closeWindow)
app.exec() 