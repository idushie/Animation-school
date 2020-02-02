from PySide2 import QtWidgets, QtGui, QtCore
import os

thisFile = os.path.abspath(__file__)
thisDir = os.path.dirname(thisFile)

iconPath = os.path.join(thisDir, 'icons')

class Button(QtWidgets.QPushButton):

    def __init__(self, icon=None):

        super(Button, self).__init__()

        #* derived options
        self.setFixedSize(60, 50)
        self.setFlat(True)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setMouseTracking(True)
        self.setAutoFillBackground(True)

        #* use attributes
        self.colorBG_idle       = 70
        self.colorBG_clicked    = 50
        self.widgetPalette      = self.palette()
        self.popMenu            = None 

        #* icon
        self.icon = icon
        self.icon_path = QtGui.QIcon(os.path.join(iconPath, self.icon + '.png'))
        self.setIcon(self.icon_path)
        self.setIconSize(QtCore.QSize(30,30))

