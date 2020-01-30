import maya.cmds as cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

if cmds.window('MainWindow', q = 1, exists = 1):
    cmds.deleteUI('MainWindow')

if cmds.windowPref('MainWindow', exists = 1):
    cmds.windowPref('MainWindow', remove =1)


class ObjectCreator(MayaQWidgetBaseMixin,QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ObjectCreator,self).__init__()

        #! Main layout and window prefs
        self.setObjectName('MainWindow')
        self.setWindowTitle('Object creator')
        self.setMinimumSize(300,200)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

       #! Menu 
        self.menu = QtWidgets.QMenuBar()
        self.edit_menu = self.menu.addMenu('Edit')
        self.edit_menu.addMenu('Save Settings')
        self.edit_menu.addMenu('Restore Settings')
        self.menu.addMenu('Help')
        self.edit_menu.setMinimumHeight(30)
        
        self.main_layout.addWidget(self.menu)
       
       
        #! Txt field
        self.txt_field_layout = QtWidgets.QHBoxLayout()
        self.txt_field_layout.setContentsMargins(10,0,10,0)

        self.main_layout.addLayout(self.txt_field_layout)
        
        self.txt_field = QtWidgets.QLineEdit()
        self.txt_field.setPlaceholderText('Object name')
        self.txt_field.setMinimumHeight(30)

        self.txt_field_layout.addWidget(self.txt_field)

        
        #! Radio buttons

        self.radio_group_box_layout = QtWidgets.QHBoxLayout()
        self.radio_group_box_layout.setContentsMargins(5,0,5,0)
        self.main_layout.addLayout(self.radio_group_box_layout)
        
        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setTitle('Objects')
        self.radio_group.setMinimumHeight(50)
        self.radio_group.setStyleSheet('background-color: black;')
        
        self.radio_group_box_layout.addWidget(self.radio_group)

        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.setContentsMargins(10,0,10,0)

        self.radio_group.setLayout(self.radio_layout)

        self.radio_Sphere = QtWidgets.QRadioButton('Sphere')
        self.radio_Sphere.setChecked(True) 
        self.radio_Cube = QtWidgets.QRadioButton('Cube')
        self.radio_Cone = QtWidgets.QRadioButton('Cone')   

        self.radio_layout.addWidget(self.radio_Sphere)
        self.radio_layout.addWidget(self.radio_Cube)
        self.radio_layout.addWidget(self.radio_Cone)

        #! Check boxes
        self.check_group_box_layout = QtWidgets.QHBoxLayout()
        self.check_group_box_layout.setContentsMargins(5,0,5,0)
        self.main_layout.addLayout(self.check_group_box_layout)

        self.check_group = QtWidgets.QGroupBox()
        self.check_group.setTitle('Options')

        self.check_group_box_layout.addWidget(self.check_group)

        self.check_box_layout = QtWidgets.QVBoxLayout()
        self.check_box_layout.setSpacing(10)
        self.check_box_layout.setContentsMargins(10,10,10,10)

        self.check_group.setLayout(self.check_box_layout)

        self.check_group = QtWidgets.QCheckBox('Put into a group')
        self.check_layer = QtWidgets.QCheckBox('Display layer/Template')
        
        self.check_box_layout.addWidget(self.check_group)
        self.check_box_layout.addWidget(self.check_layer)
        

        #! Translate objects

        self.translate_box_layout = QtWidgets.QHBoxLayout()
        self.translate_box_layout.setContentsMargins(5,0,5,0)
        self.main_layout.addLayout(self.translate_box_layout)

        self.translate_group = QtWidgets.QGroupBox()
        self.translate_group.setTitle('Translate objects')
        
        self.translate_box_layout.addWidget(self.translate_group)

        self.translate_layout = QtWidgets.QHBoxLayout()
        

        self.translate_group.setLayout(self.translate_layout)

        #*Combo box
        self.combo_axis = QtWidgets.QComboBox()
        self.combo_axis.addItems(['X','Y','Z'])

        self.translate_layout.addWidget(self.combo_axis)

        #* Create slider value txt field
        self.slider_value_txt = QtWidgets.QLineEdit()
        self.translate_layout.addWidget(self.slider_value_txt)
        self.slider_value_txt.setMaximumWidth(40)
        self.slider_value_txt.setText('0')

        #* Create slider 
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.translate_layout.addWidget(self.slider)
        
        self.slider.valueChanged.connect(self.slider_value)

        self.slider.setMaximum(100)

        #! Create buttons
        self.Create_btn = QtWidgets.QPushButton('Create')
        self.Cancel_btn = QtWidgets.QPushButton('Cancel')
        
        self.btns_layout = QtWidgets.QHBoxLayout()
        self.btns_layout.setContentsMargins(5,0,5,10)
        self.main_layout.addLayout(self.btns_layout)

        self.btns_layout.addWidget(self.Create_btn)
        self.btns_layout.addWidget(self.Cancel_btn)
       
        self.Create_btn.clicked.connect(self.create_obj)
        self.Cancel_btn.clicked.connect(self.close)

        

    def create_obj(self):

        if self.radio_Sphere.isChecked():
            cmds.polySphere(n = self.txt_field.text())

        elif self.radio_Cube.isChecked():
            cmds.polyCube()
        else:
            cmds.polyCone()
        
        if self.check_group.isChecked():

            cmds.group(n = self.txt_field.text()+'_grp')

        if self.check_layer.isChecked():

            layer = cmds.createDisplayLayer()
            cmds.setAttr("{}.displayType".format(layer),1)
        
        cmds.setAttr('.t' + self.combo_axis.currentText().lower(), self.slider.value())
    
    
    def slider_value(self, value):
      
        self.slider_value_txt.setText(str(value))




a = ObjectCreator()
a.show()

