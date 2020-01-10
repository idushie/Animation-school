from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QPoint

if cmds.window('MainWindow', q = 1, exists = 1):
    cmds.deleteUI('MainWindow')

if cmds.windowPref('MainWindow', exists = 1):
    cmds.windowPref('MainWindow', remove =1)
 

class SelectonSet(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, parent = None):

        super(SelectonSet, self).__init__()

        #! Main layout and window prefs
        self.setObjectName('MainWindow')
        self.setWindowTitle('Selection set')
        

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        self.setLayout(self.main_layout)
       
        self.select_set_btn_layout = QtWidgets.QHBoxLayout()
        self.select_set_btn_layout.setContentsMargins(2,2,2,2)
        self.select_set_btn_layout.setSpacing(2)
        self.setAutoFillBackground(1)
        color = 50
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        self.main_layout.addLayout(self.select_set_btn_layout)
        
        
        self.create_set_btn_layout = QtWidgets.QVBoxLayout()
        self.create_set_btn_layout.setContentsMargins(5,5,5,5)
        self.main_layout.addLayout(self.create_set_btn_layout)

        self.create_set_btn = QtWidgets.QPushButton('Create set')
        self.create_set_btn.clicked.connect(self.show_window)
        self.create_set_btn.setObjectName('CreateSetButton')
        self.create_set_btn.setMinimumWidth(80)
        self.buttonStyle = """
            QPushButton#CreateSetButton{
                background-color: rgb(255,20,147);
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font bold 14px;
                padding: 6px;
                color: black;
                font-weight: 20px;
                min-width: 80px;
                min-height: 30px;
                font-weight: 900;

 
            }
            QPushButton#CreateSetButton:hover {
                background-color: rgb(128,0,128);
                color: white;
                border-style: inset;
            
            }
            """
        self.create_set_btn.setStyleSheet(self.buttonStyle)
        self.create_set_btn_layout.addWidget(self.create_set_btn)
    
    def create_set(self):
        
        selection_set = cmds.ls (sl=1, l=1)
        selection_set_shapes = cmds.listRelatives(selection_set, c=1, f=1)

        selection_list = []
        if selection_set_shapes == None:
            pass
        else:
            for i in selection_set_shapes:
                if cmds.objectType(i) == 'nurbsCurve':
                    selection_list.append(i)
                
        return selection_list
        
    @QtCore.Slot(str)
    def receiveSignal(self, text = None):
        
        self.set = self.create_set()

        self.set_button = CustomWidget(object_set = self.set)
        self.select_set_btn_layout.addWidget(self.set_button)
        self.set_button.setText(text)
        self.adjustSize()
        
        self.oldPos = text 

    def show_window(self):

        self.a = SelectColorName()
        self.a.show()
        
        self.a.buttonSignal.connect(self.receiveSignal)
    
    def mousePressEvent(self, event):

        if event.button() == QtCore.Qt.MidButton:
            self.setMouseTracking(True)
            self.oldPos = event.globalPos() # Position of cursor
            

            super(SelectonSet, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MidButton:
            delta = QPoint (event.globalPos() - self.oldPos) # 
            
            self.move(self.x() + delta.x(), self.y() + delta.y())# 
            self.oldPos = event.globalPos()
            
            super(SelectonSet, self).mouseMoveEvent(event)


class SelectColorName(MayaQWidgetBaseMixin, QtWidgets.QDialog):
 
    buttonSignal = QtCore.Signal(str)

    def __init__(self, parent = SelectonSet):

        super(SelectColorName, self).__init__()

        #! Main layout and window prefs
        self.setObjectName('MainWindow2')
        self.setWindowTitle('Edit text')
        self.setModal(True)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)
        
        self.txt_field_layout = QtWidgets.QHBoxLayout()
        self.txt_field_layout.setContentsMargins(10,10,10,0)

        self.main_layout.addLayout(self.txt_field_layout)
        
        self.txt_field = QtWidgets.QLineEdit()
        self.txt_field.setPlaceholderText('Set name')
        self.txt_field.setMinimumHeight(30)
        self.txt_field.setObjectName('txt_field')
        self.text_field_style = """
            QLineEdit#txt_field{
                border: 2px solid gray;
                border-radius: 10px;
                padding: 0 8px;
                background: yellow;
                color: black;
                selection-background-color: darkgray;
            }
            """
        self.txt_field.setStyleSheet(self.text_field_style)
        self.txt_field_layout.addWidget(self.txt_field)
    
        #! OK Button
        self.btn2_layout = QtWidgets.QHBoxLayout()
        self.btn2_layout.setContentsMargins(10,0,10,10)
        self.main_layout.addLayout(self.btn2_layout)
        
        self.btn2 = QtWidgets.QPushButton('Ok')
        self.btn2_layout.addWidget(self.btn2)


        self.btn2.clicked.connect(self.send_signal)

    def send_signal(self):

        text = self.txt_field.text()

        if text:
            self.buttonSignal.emit(text)
            self.close()
    
    
    

class CustomWidget(QtWidgets.QWidget):

    position_signal = QtCore.Signal(str)

    def __init__(self, object_set = None):

        super(CustomWidget, self).__init__()

        self.set = object_set

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(2,1,1,1)
        
        self.setLayout(self.main_layout)

        #* set background color
        self.setAutoFillBackground(1)
        color = 90
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        self.label = QtWidgets.QLabel()
        self.main_layout.addWidget(self.label)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter) 

        self.setMinimumSize(self.label.minimumWidth(),60)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showPopup)

        self.popupMenu = QtWidgets.QMenu(self)
        self.add_selection = self.popupMenu.addAction(QtWidgets.QAction('Add selection', self,
                                                                            triggered=self.addSelection))
        
        self.remove_selection = self.popupMenu.addAction(QtWidgets.QAction('Remove selection', self,
                                                                            triggered=self.removeSelection))
    
    
    def addSelection(self):
        
        selection_set = cmds.ls (sl=1, l=1)
        selection_set_shapes = cmds.listRelatives(selection_set, c=1, f=1)

        selection_list = []
        if selection_set_shapes == None:
            pass
        else:
            for i in selection_set_shapes:
                if cmds.objectType(i) == 'nurbsCurve':
                    selection_list.append(i)

            for i in selection_list:
                if i in self.set:
                    continue
                else:
                    self.set.append(i)

        
    def removeSelection(self):

        selection_set = cmds.ls (sl=1, l=1)
        selection_set_shapes = cmds.listRelatives(selection_set, c=1, f=1)
        
        for i in selection_set_shapes:
            self.set.remove(i)

    def showPopup(self,position):
         self.popupMenu.exec_(self.mapToGlobal(position))

    def select_set(self):

        cmds.select(self.set)

    def setText(self, text = ''):
        
        self.text = text
        self.label.setText(self.text)
    
    def mouseReleaseEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            cmds.select(self.set)

            self.setAutoFillBackground(1)
            color = 90
            self.p = self.palette()
            self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
            self.setPalette(self.p)
        
            super(CustomWidget, self).mouseReleaseEvent(e)
        

    def mousePressEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            self.setAutoFillBackground(1)
            color = 0
            self.p = self.palette()
            self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
            self.setPalette(self.p)
        
        if e.button() == QtCore.Qt.MidButton:
            self.oldPos = e.globalPos()
            self.send_signal(self.oldPos)

            super(CustomWidget, self).mousePressEvent(e)

    def mouseMoveEvent(self, event):
        
        self.oldPos = event.globalPos()
        self.send_signal(self.oldPos)
        
        super(CustomWidget, self).mouseMoveEvent(event) 

    def send_signal(self, pos):

        self.position_signal.emit(pos)

myUI = SelectonSet()
myUI.show()
