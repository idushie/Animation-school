import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from random import randint, choice

if cmds.window('MainWindow', q = 1, exists = 1):
    cmds.deleteUI('MainWindow')

if cmds.windowPref('MainWindow', exists = 1):
    cmds.windowPref('MainWindow', remove =1)


class MainWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, parent = None):

        super(MainWindow, self).__init__()

        self.COLOR = [(220, 20, 60), (50, 205, 50), (0, 0, 255), (148, 0, 211), (255, 165, 0), (219, 112, 147)]
        self.setFixedSize(300,300)
        self.setObjectName('MainWindow')

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setSpacing(10)
        self.main_layout.addLayout(self.btn_layout)

        self.widget1 = CustomWidget()
        self.widget1.signal.connect(self.resive_signal)
        self.widget1.label.setText('Widget1')
        
        self.widget2 = CustomWidget()
        self.widget2.signal.connect(self.resive_signal)
        self.widget2.label.setText('Widget2')

        self.btn_layout.addWidget(self.widget1)
        self.btn_layout.addWidget(self.widget2)

    def resive_signal (self, widget_id):
        
        if widget_id == str(self.widget1):
            
            self.random_color = choice(self.COLOR)
            
            self.widget2.change_color(self.random_color)

        elif widget_id == str(self.widget2):

            self.random_color = choice(self.COLOR)
            
            self.widget1.change_color(self.random_color)
    
class CustomWidget(QtWidgets.QWidget):

    signal =  QtCore.Signal(str)

    def __init__(self, parent = None):

        super(CustomWidget, self).__init__()

        self.setupUI()

    def setupUI(self):
        
        self.setFixedSize(100, 40)
        
        self.setAutoFillBackground(1)
        color = 120
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color, color, color))
        self.setPalette(self.p)
        
        
        # main Layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.mainLayout)

        self.label = QtWidgets.QLabel()
        self.mainLayout.addWidget(self.label)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def change_color(self, color):

        
        self.setAutoFillBackground(1)
        self.p = self.palette() #QPalette
        color1, color2, color3 = color
        
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color1, color2, color3))

        self.setPalette(self.p)
    
    def mouseReleaseEvent(self, e):
        
        self.sendSignal()

        # do It
        color = 120
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        
        super(CustomWidget, self).mouseReleaseEvent(e)
        
   
    def mousePressEvent(self, e):

        color = 0
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        super(CustomWidget, self).mousePressEvent(e)


    def sendSignal(self):
        
        self.signal.emit( str(self))


a = MainWindow()
a.show()


        



