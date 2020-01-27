from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds
import time

"""
Custom Signal - Minimal Setup
"""

class MyChildChildDialog(QtWidgets.QDialog):

    buttonSignal = QtCore.Signal(str) # create a static attribute

    def __init__(self, parent = None):

        super(MyChildChildDialog, self).__init__()

        self.setFixedSize(300,300)
        self.setObjectName("myCustomSignalExampleMyChildChildDialogWindow_Pointer")
        self.setWindowTitle("Child Child")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        #simple text field
        self.textField = QtWidgets.QLineEdit()

        #button
        self.button = QtWidgets.QPushButton("Run Another Window")
        self.button.clicked.connect(self.buttonPressed)
MainWindow
        #compose main layout
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.button)

    def buttonPressed(self):

        self.buttonSignal.emit(str(self))


class MyChildDialog(QtWidgets.QDialog):

    buttonSignal = QtCore.Signal(str) # create a static attribute

    def __init__(self, parent = None):

        super(MyChildDialog, self).__init__()

        self.setFixedSize(300,300)
        self.setObjectName("myCustomSignalExampleChildWindow_Pointer")
        self.setWindowTitle("Child")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        #simple text field
        self.textField = QtWidgets.QLineEdit()

        #button
        self.button = QtWidgets.QPushButton("Run Child Child Window") #("Emit Signal") #
        self.button.clicked.connect(self.buttonPressed)

        #compose main layout
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.button)

    def buttonPressed(self):

        # text = self.textField.text()

        # if text:
        #     self.buttonSignal.emit(text)

        self.chld = MyChildChildDialog(parent = self)
        self.chld.show()
        self.chld.buttonSignal.connect(self.receiveSignalOne)

    @QtCore.Slot(str)
    def receiveSignalOne(self, text):

        self.buttonSignal.emit(text)



class MyParentDialog(QtWidgets.QDialog):

    def __init__(self, parent = None):

        super(MyParentDialog, self).__init__()

        self.setFixedSize(300,300)
        self.setObjectName("myCustomSignalExampleParentWindow_Pointer")
        self.setWindowTitle("Parent")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)


        #simple text field
        self.textField = QtWidgets.QLineEdit()

        #button
        self.button = QtWidgets.QPushButton("Run Another Window")
        self.button.clicked.connect(self.runChildWindow)

        #compose main layout
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.button)

    def runChildWindow(self):

        self.chld = MyChildDialog(parent = self)
        self.chld.show()
        self.chld.buttonSignal.connect(self.receiveSignal)


    @QtCore.Slot(str)
    def receiveSignal(self, text = None):

        print(text)
        self.textField.setText(text)


def main():
    
    
    if cmds.window("myCustomSignalExampleParentWindow_Pointer", exists = 1):
        cmds.deleteUI("myCustomSignalExampleParentWindow_Pointer")

    if cmds.windowPref("myCustomSignalExampleParentWindow_Pointer", exists = 1):
        cmds.windowPref("myCustomSignalExampleParentWindow_Pointer", remove = 1)

    global myCustomSignalExampleParentWindow

    myCustomSignalExampleParentWindow = MyParentDialog()
    myCustomSignalExampleParentWindow.show()

main()
