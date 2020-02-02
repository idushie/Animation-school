from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from shiboken2 import wrapInstance
import re
from maya.OpenMayaUI import MQtUtil
import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QPoint
import os
from button import Button

if cmds.window('MainWindow', q = 1, exists = 1):
    cmds.deleteUI('MainWindow')

if cmds.windowPref('MainWindow', exists = 1):
    cmds.windowPref('MainWindow', remove =1)

def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = MQtUtil.mainWindow() # Python API 1.0
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget) 


#thisFile = os.path.abspath(__file__)
#thisDir = os.path.dirname(thisFile)

#iconPath = os.path.join(thisDir, 'icons')

collection_sets = []

class SelectonSet(MayaQWidgetBaseMixin, QtWidgets.QWidget):

    def __init__(self, parent=None):

        super(SelectonSet, self).__init__()

        self.COLLECTION_SET = []

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        #! Main layout and window prefs
        self.setObjectName('MainWindow')
        self.setWindowTitle('Selection set')
        
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.container = QtWidgets.QWidget()
        self.main_layout.addWidget(self.container)

        self.container.setStyleSheet('background-color: balck;')

       #! Select set btn
        self.select_set_btn_layout = QtWidgets.QHBoxLayout()
        self.select_set_btn_layout.setContentsMargins(5,5,5,5)
        self.select_set_btn_layout.setSpacing(2)
        self.container.setLayout(self.select_set_btn_layout)
        
        #! Create set btn
        self.create_set_btn_layout = QtWidgets.QVBoxLayout()
        self.create_set_btn_layout.setContentsMargins(5,5,5,5)
        self.main_layout.addLayout(self.create_set_btn_layout)

        self.close_btn_layout = QtWidgets.QVBoxLayout()
        self.close_btn_layout.setContentsMargins(5,5,5,5)
        self.close_btn_layout.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.main_layout.addLayout(self.close_btn_layout)

    
        self.create_set_btn = Button('add_btn')
        self.create_set_btn.clicked.connect(self.show_window)
        self.create_set_btn.setMaximumWidth(80)
        self.create_set_btn.setMinimumWidth(80)

        #self.create_set_btn.setObjectName('CreateSetButton')
        #self.icon_path = os.path.join(iconPath, 'add_btn.png')
        
        #self.create_set_btn.setIcon(QtGui.QIcon(self.icon_path))
        self.create_set_btn.setIconSize(QtCore.QSize(80,40))
        self.create_set_btn_layout.addWidget(self.create_set_btn)

        self.reveal_data()
 
    def reveal_data(self ):

        global collection_sets

        try: 
            cmds.scriptNode( 'selection_setNode', executeBefore=True)
        except ValueError:    
            pass

        if collection_sets:

            list_length = len(collection_sets)

            #* Info about widget consist of list set, color, text label thats why div by 3
            number_of_widgets  = list_length / 3

            for widget in range(number_of_widgets):

                widget_set, widget_color , widget_text = collection_sets[:3]

                collection_sets = collection_sets[3:]


                self.COLLECTION_SET.append(widget_set)
                self.COLLECTION_SET.append(widget_color)
                self.COLLECTION_SET.append(widget_text)

                self.create_set_button(sel_set = widget_set, color = widget_color, text = widget_text)

    def deleteSet(self, setPointer):

        if self.select_set_btn_layout.count(): # if layout has any children
            for i in range(self.select_set_btn_layout.count()):
                item = self.select_set_btn_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    if str(widget) == setPointer:
                        
                        self.COLLECTION_SET.remove(widget.set)
                        self.COLLECTION_SET.remove(widget.color)
                        self.COLLECTION_SET.remove(widget.text)

                        save_info = 'collection_sets={}'.format(str(self.COLLECTION_SET))
                        cmds.scriptNode( 'selection_setNode', e=True, bs=save_info, stp='python' )
                        
                        widget.deleteLater()
    
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
    def receive_signal_color(self, color_text_list = [],):
        
        self.text, self.color = color_text_list
        self.set = self.create_set()
        
        if self.set not in self.COLLECTION_SET:

            self.COLLECTION_SET.append(self.set)
            self.COLLECTION_SET.append(self.color)
            self.COLLECTION_SET.append(self.text)

            save_info = 'collection_sets={}'.format(str(self.COLLECTION_SET))

            try:
                cmds.scriptNode( 'selection_setNode', e=True, bs=save_info, stp='python' )
                
            except ValueError:

                cmds.scriptNode(scriptType=2, beforeScript=save_info, 
                                name='selection_setNode', sourceType='python')
        

        self.create_set_button(sel_set = self.set, color = self.color, text = self.text)
        
    def create_set_button(self, sel_set = [], color = '', text = ''):

        self.set_button = CustomWidget(object_set = sel_set, color=color)
        self.set_button.doRemove.connect(self.deleteSet)
        self.select_set_btn_layout.addWidget(self.set_button)

        self.set_button.setText(text)
        
    def show_window(self):

        self.color_widget = SelectColorName()
        self.color_widget.show()
        #self.color_widget.color_signal.connect(self.receive_signal_color)
        self.color_widget.buttonSignal.connect(self.receive_signal_color)
        
    
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

    buttonSignal = QtCore.Signal(list)
    color_signal = QtCore.Signal(str)

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
        self.txt_field_layout.addWidget(self.txt_field)

        self.txt_field.returnPressed.connect(self.send_signal)
        
        #! GroupBox and radio buttons
        self.radio_group_box_layout = QtWidgets.QVBoxLayout()
        self.radio_group_box_layout.setContentsMargins(5,0,5,0)
        self.main_layout.addLayout(self.radio_group_box_layout)

        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setMinimumHeight(50)
        
        self.radio_group_box_layout.addWidget(self.radio_group)

        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.setContentsMargins(5,0,5,0)

        self.radio_group.setLayout(self.radio_layout)

        self.radioStyle1 = """
            QRadioButton{
                background-color: red
            }
            QRadioButton:indicator {
                width: 10px;
                height: 10px;
                subcontrol-position: center;
                background-color: red
            
            }
            QRadioButton:checked  {
                border: 1px inset beige
            }
            """
        self.radio_group.setStyleSheet(self.radioStyle1) 

        COLOR = ['Crimson', 'LimeGreen', 'Blue','DarkViolet','Orange','PaleVioletRed']

        self.radio_color_1 = QtWidgets.QRadioButton()
        self.radio_color_1.setChecked(True)
        self.radio_color_2 = QtWidgets.QRadioButton()
        self.radio_color_3 = QtWidgets.QRadioButton()
        self.radio_color_4 = QtWidgets.QRadioButton()
        self.radio_color_5 = QtWidgets.QRadioButton()
        self.radio_color_6 = QtWidgets.QRadioButton()

        self.radio_color_1.setFixedSize(20, 20)
        self.radio_color_2.setFixedSize(20, 20)
        self.radio_color_3.setFixedSize(20, 20)
        self.radio_color_4.setFixedSize(20, 20)
        self.radio_color_5.setFixedSize(20, 20)
        self.radio_color_6.setFixedSize(20, 20)

        self.radio_layout.addWidget(self.radio_color_1)
        self.radio_layout.addWidget(self.radio_color_2)
        self.radio_layout.addWidget(self.radio_color_3)
        self.radio_layout.addWidget(self.radio_color_4)
        self.radio_layout.addWidget(self.radio_color_5)
        self.radio_layout.addWidget(self.radio_color_6)

        #*Color for each radio btn
        self.radi_style_1 = 'QRadioButton{background-color:'+ 'LightCoral' +'} QRadioButton:indicator { background-color:' + 'LightCoral' + '}'
        self.radi_style_2 = 'QRadioButton{background-color:'+ 'LimeGreen' +'} QRadioButton:indicator { background-color:' + 'LimeGreen' + '}'
        self.radi_style_3 = 'QRadioButton{background-color:'+ 'SteelBlue' +'} QRadioButton:indicator { background-color:' + 'SteelBlue' + '}'
        self.radi_style_4 = 'QRadioButton{background-color:'+ 'MediumPurple' +'} QRadioButton:indicator { background-color:' + 'MediumPurple' + '}'
        self.radi_style_5 = 'QRadioButton{background-color:'+ 'Orange' +'} QRadioButton:indicator { background-color:' + 'Orange' + '}'
        self.radi_style_6 = 'QRadioButton{background-color:'+ 'PaleVioletRed' +'} QRadioButton:indicator { background-color:' + 'PaleVioletRed' + '}'

        self.radio_color_1.setStyleSheet(self.radi_style_1)
        self.radio_color_2.setStyleSheet(self.radi_style_2)
        self.radio_color_3.setStyleSheet(self.radi_style_3)
        self.radio_color_4.setStyleSheet(self.radi_style_4)
        self.radio_color_5.setStyleSheet(self.radi_style_5)
        self.radio_color_6.setStyleSheet(self.radi_style_6)

    def send_signal(self):

        list_signal = []
        text = self.txt_field.text()
        if text:
            list_signal.append(text)

            if self.radio_color_1.isChecked():

                list_signal.append('LightCoral')

                self.buttonSignal.emit(list_signal)

            elif self.radio_color_2.isChecked():
                list_signal.append('LimeGreen')
                self.buttonSignal.emit(list_signal)

            elif self.radio_color_3.isChecked():
                list_signal.append('SteelBlue')
                self.buttonSignal.emit(list_signal)

            elif self.radio_color_4.isChecked():
                list_signal.append('MediumPurple')
                self.buttonSignal.emit(list_signal)

            elif self.radio_color_5.isChecked():
                list_signal.append('Orange')
                self.buttonSignal.emit(list_signal)

            elif self.radio_color_6.isChecked():
                list_signal.append('PaleVioletRed')
                self.buttonSignal.emit(list_signal)

        
            self.close()
class CustomWidget(QtWidgets.QWidget):

    position_signal = QtCore.Signal(str)
    doRemove = QtCore.Signal(str)

    def __init__(self, object_set = None, color = 'red'):

        super(CustomWidget, self).__init__() 

        self.set = object_set
        self.color = color


        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(1,1,1,1)
        self.main_layout.setSpacing(0)
        
        self.setLayout(self.main_layout)

        self.label = QtWidgets.QLabel()
        self.label.setVisible(1)
        self.main_layout.addWidget(self.label)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.name_change_field = QtWidgets.QLineEdit()
        self.name_change_field.setVisible(0)
        self.name_change_field.setMinimumWidth(60)
        self.name_change_field.setMinimumHeight(50)
        self.name_change_field.returnPressed.connect(self.rename_presed)
        self.name_change_field.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.main_layout.addWidget(self.name_change_field)

        self.label.setStyleSheet('font: 14px; color: black;')
        self.widget_style_sheet = '''
                background-color: {};
                border-radius: 5px;
        '''.format (self.color)

        self.setStyleSheet(self.widget_style_sheet)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showPopup)
        self.popupMenu = QtWidgets.QMenu()

        self.add_selection = self.popupMenu.addAction(QtWidgets.QAction('Add selection', self,
                                                                            triggered=self.addSelection))
        
        self.remove_selection = self.popupMenu.addAction(QtWidgets.QAction('Remove selection', self,
                                                                            triggered=self.removeSelection))

        self.delete_set = self.popupMenu.addAction(QtWidgets.QAction('Delete set', self,
                                                                            triggered=self.delSelectionSet))                                                                    
    
    def rename_set(self):

        self.setStyleSheet(self.widget_style_sheet)
        set_name = self.label.text()
        self.name_change_field.setText(set_name)
        self.label.setVisible(0)
        self.name_change_field.setVisible(1)
        
    
    def rename_presed(self):

        set_name = self.name_change_field.text()
        self.label.setText(set_name)
        self.label.setVisible(1)
        self.name_change_field.setVisible(0)
        self.setStyleSheet(self.widget_style_sheet)
    
    def delSelectionSet(self):

        self.doRemove.emit(str(self))

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
    
    def mouseDoubleClickEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            
            self.rename_set()
            self.setStyleSheet(self.widget_style_sheet)


            super(CustomWidget, self).mouseDoubleClickEvent(e)

    def mouseReleaseEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            cmds.select(self.set)

            self.setStyleSheet(self.widget_style_sheet)
        
            super(CustomWidget, self).mouseReleaseEvent(e)
        

    def mousePressEvent(self, e):
        
        if e.button() == QtCore.Qt.LeftButton:
            self.widget_style_sheet_press = '''
                background-color: black;
                border-radius: 5px;
        '''
            self.setStyleSheet(self.widget_style_sheet_press)
        
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
#myUI.adjustSize()
#myUI.move(300,500)
myUI.show()



myUI.COLLECTION_SET
