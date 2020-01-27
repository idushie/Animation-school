from PySide2 import QtWidgets, QtGui, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds
# Maya Python API 2.0
from maya.api.OpenMaya import MGlobal
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
# Maya Python API 1.0
from maya.OpenMayaUI import MQtUtil

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


class TestDialog(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(TestDialog, self).__init__()

        #! Main layout and window prefs
        self.setObjectName('MainWindow')
        self.setWindowTitle('Selection set')
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.radio_group_box_layout = QtWidgets.QHBoxLayout()
        self.radio_group_box_layout.setContentsMargins(5,0,5,0)
        self.main_layout.addLayout(self.radio_group_box_layout)
        
        self.btn = QtWidgets.QPushButton('Push me')
        self.label = QtWidgets.QLabel('FUCK QT')
        self.main_layout.addWidget(self.label)
        self.label_style = """
            QLabel{
                background-color: DarkViolet;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 6px;
                color: black;
                font-weight: 20px;
                min-width: 80px;
                min-height: 30px;
                font-weight: 900;
            }
            """
        self.label.setStyleSheet('font: bold 14px; color: black;') 
        

        self.main_layout.addWidget(self.btn)

        self.buttonStyle = """
            QPushButton{
                background-color: DarkViolet;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                padding: 6px;
                color: black;
                font-weight: 20px;
                min-width: 80px;
                min-height: 30px;
                font-weight: 900;
            }
            """
        self.btn.setStyleSheet(self.buttonStyle)

        #! GroupBox and radio buttons
        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setTitle('Objects')
        self.radio_group.setMinimumHeight(50)
        
        self.radio_group_box_layout.addWidget(self.radio_group)

        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.setContentsMargins(5,0,5,0)

        self.radio_group.setLayout(self.radio_layout)

        self.radio_Sphere = QtWidgets.QRadioButton('Python')
        self.radio_Sphere.setFixedSize(30, 30)
        self.radio_Sphere.setChecked(True)
        self.radio_Sphere.setObjectName('Red')

        self.radio_Cube = QtWidgets.QRadioButton()
        self.radio_Cube.setFixedSize(30, 30)
        self.radio_Cube.setObjectName('Green')

        self.radio_Cone = QtWidgets.QRadioButton()
        self.radio_Cone.setFixedSize(30, 30)
        self.radio_Cone.setObjectName('Blue')   

        self.radio_layout.addWidget(self.radio_Sphere)
        self.radio_layout.addWidget(self.radio_Cube)
        self.radio_layout.addWidget(self.radio_Cone)
        self.radioStyle1 = """
            QRadioButton{
                background-color: red
            }
            QRadioButton:indicator {
                width: 20px;
                height: 20px;
                subcontrol-position: center;
                background-color: red
            
            }
            QRadioButton:checked  {
                border: 1px inset beige
            }
            """
        i = 'DarkViolet'
        self.radi_style = 'QRadioButton{background-color:'+ i +'} QRadioButton:indicator { background-color:' + i + '}'
        
        self.radio_group.setStyleSheet(self.radioStyle1) 
        self.radio_Sphere.setStyleSheet(self.radi_style)   

        self.radioStyle2 = """
            QRadioButton#Green{
                background-color: green
            }
            QRadioButton#Green:indicator {
                width: 20px;
                height: 20px;
                subcontrol-position: center;
                background-color: green
            
            }
            QRadioButton#Green:checked  {
                
                border: 1px inset beige
            }
            """
        self.radio_Cube.setStyleSheet(self.radioStyle2)

        self.radioStyle3 = """
            QRadioButton#Blue{
                background-color: blue
            }
            QRadioButton#Blue:indicator {
                width: 20px;
                height: 20px;
                subcontrol-position: center;
                background-color: blue
                
            }
            QRadioButton#Blue:checked  {
                
                border: 1px inset beige
            }

            """
        self.radio_Cone.setStyleSheet(self.radioStyle3)


test_dialog = TestDialog()
test_dialog.move(300,500)
test_dialog.resize(300 , 300)
test_dialog.show()
