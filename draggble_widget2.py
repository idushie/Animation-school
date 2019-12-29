from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QPoint
import os


if cmds.window('MainWindow', q = 1, exists = 1):
    cmds.deleteUI('MainWindow')

if cmds.windowPref('MainWindow', exists = 1):
    cmds.windowPref('MainWindow', remove =1)


thisFile = os.path.abspath(__file__)
thisDir = os.path.dirname(thisFile)

iconPath = os.path.join(thisDir, 'icons')


class Test(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, parent = None):

        super(Test, self).__init__()

        #! Main layout and window prefs
        self.setObjectName('MainWindow')
        self.setWindowTitle('Selection set')
        

        self.main_layout = QtWidgets.QHBoxLayout()
        
        self.setLayout(self.main_layout)
       
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.btn_layout)
        
        self.btn2 = QtWidgets.QPushButton('Close')
        self.btn = Button()
        self.btn_layout.addWidget(self.btn)
        self.btn_layout.addWidget(self.btn2)
        
        self.txt_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.txt_layout)

        self.txt = QtWidgets.QLabel('Python')
        self.txt_layout.addWidget(self.txt)

        self.btn2.clicked.connect(self.close)
        self.btn.setMouseTracking(True)
    
    
    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.MidButton:
            self.setMouseTracking(True)
            self.oldPos = event.globalPos() # Position of cursor
            

            super(Test, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MidButton:
            delta = QPoint (event.globalPos() - self.oldPos) # 
            
            self.move(self.x() + delta.x(), self.y() + delta.y())# 
            self.oldPos = event.globalPos()
            
            super(Test, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        
        self.setMouseTracking(False)
    
    
    def receiveSignal(self, pos = None):
        
        self.oldPos = pos  

class Button (QtWidgets.QPushButton):

    buttonSignal = QtCore.Signal(str)

    def __init__(self, object_set = None):

        super(Button, self).__init__()

        self.setText('Click me')
        
        


    def mousePressEvent(self, event):
        
        
    
        if event.button() == QtCore.Qt.MidButton:
            self.oldPos = event.globalPos()
            self.send_signal(self.oldPos)


        super(Button, self).mousePressEvent(event)
        
    def mouseMoveEvent(self, event):
        
        self.oldPos = event.globalPos()
        self.send_signal(self.oldPos)
        super(Button, self).mouseMoveEvent(event) 

  
    def send_signal(self, pos):

        self.buttonSignal.emit(pos)



myUi = Test()
myUi.move(300,500)
myUi.show()