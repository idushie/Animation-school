from PySide2 import QtWidgets, QtCore, QtGui
import maya.cmds as cmds 
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin



class CustomWidget(QtWidgets.QWidget):
    
    fix =  QtCore.Signal(str)
    
    def __init__(self, objectPath = None):
        super(CustomWidget, self).__init__()
        
        self.objectPath = objectPath
        self.objectName = self.objectPath.split('|')[-1]
        
        self.setObjectName(self.objectName)
        
        self.setupUI()
        
        
    def getObjectFullPath(self):
        return self.objectPath
        
        
    def getObjectName(self):
        return self.objectName
        
        
    def setupUI(self):
        
        self.setFixedSize(375, 40)
        
        self.setAutoFillBackground(1)
        color = 75
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        
        
        # main Layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.mainLayout.setSpacing(20)
        self.setLayout(self.mainLayout)
        
        # checkbox
        
        self.chkBox = QtWidgets.QCheckBox()
        self.mainLayout.addWidget(self.chkBox)
        

        # Label
        self.labl = QtWidgets.QLabel(self.objectName)
        self.labl.setFixedSize(285, 30)
        self.mainLayout.addWidget(self.labl)
        
        # button
        
        self.btn = QtWidgets.QPushButton('Fix')
        self.btn.setObjectName('MySuperButton')
        self.button2Style = """
            QPushButton#MySuperButton{
                background-color: rgb(109,113,168);
                border-radius: 10px;
                min-width: 30px;
                min-height: 30px;
                font-weight: 900;

 
            }
            QPushButton#MySuperButton:hover {
                background-color: rgb(255,133,198);
                min-width: 30px;
                min-height: 30px;  
            }
            """
        self.btn.setStyleSheet(self.button2Style)
        
        self.btn.clicked.connect(self.sendSignal)
        
        
        
        self.mainLayout.addWidget(self.btn)
        
    
    def isChecked(self):
        
        
        return self.chkBox.isChecked()
        
        
    def sendSignal(self):
        
        self.fix.emit( self.getObjectFullPath() )
        
        
    def mouseReleaseEvent(self, e):
        
        # do It
        color = 75
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        
        
        cmds.select( self.getObjectFullPath() )
        
        super(CustomWidget, self).mouseReleaseEvent(e)
        
   
    def mousePressEvent(self, e):
        color = 120
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        super(CustomWidget, self).mousePressEvent(e)
        
        
    def enterEvent(self, e):
        color = 85
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        
        super(CustomWidget, self).enterEvent(e)
        
        
    def leaveEvent(self, e):
        color = 75
        self.p = self.palette() #QPalette
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)
        self.setCursor(QtCore.Qt.ArrowCursor)
        
        super(CustomWidget, self).leaveEvent(e)


class SceneChecker(MayaQWidgetDockableMixin, QtWidgets.QDockWidget):
    
    def __init__(self):
        
        super(SceneChecker, self).__init__()
        
        self.setObjectName('mySceneChecker')
        
        self.setupUI()
        
        
    def checkZeroTransforms(self):
        
        objects = cmds.ls(l=1, type='mesh')

        objectsTransforms = cmds.listRelatives(objects, p=1, f=1)
        
        results = []
        
        for i in objectsTransforms:
        
            rotation = cmds.xform(i, q=1, ws=1, ro=1)
            
            translation = cmds.xform(i, q=1, ws=1, t=1)
            
            if any(rotation) or any(translation):
                results.append(i)
                
        return results
        
        
    def fixZeroTransforms(self, obj = None):
        
        if not obj:
            return
            
        cmds.xform(obj, ro=(0,0,0), t=(0,0,0))    
        
    
    def runChecker(self):
        
        if self.scroll_layout.count(): # if layout has any children
          for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            widget = item.widget()
            if widget:
              widget.deleteLater()
        
        badObjects = self.checkZeroTransforms()
        
        if badObjects:
            for i in badObjects:
                buttonA = CustomWidget(objectPath = i)
                buttonA.fix.connect(self.fixZeroTransforms)
                self.scroll_layout.addWidget(buttonA)
                
                
    def runFix(self):
        
        widgetList = []
        widgetListFull = [] 
        
        if self.scroll_layout.count(): # if layout has any children
        
          for i in range(self.scroll_layout.count()):
              
            item = self.scroll_layout.itemAt(i)
            widget = item.widget()
            
            if widget.isChecked():
                widgetList.append(widget)
            
            widgetListFull.append(widget)    
                
        if widgetList:
            for i in widgetList:
                abc = i.getObjectFullPath()
                self.fixZeroTransforms(obj = abc)  
                i.deleteLater()
        else:
            for i in widgetListFull:
                abc = i.getObjectFullPath()
                self.fixZeroTransforms(obj = abc)  
                i.deleteLater()
        
                
        
    def setupUI(self):
        
        #properties
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(500)
        self.setWindowTitle('Scene Checker')
        self.setDockableParameters(widht = 400)
        
        self.mainWidget = QtWidgets.QWidget()
        self.setWidget(self.mainWidget)
        
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(10)
        self.mainLayout.setContentsMargins(5,5,5,5)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.mainWidget.setLayout(self.mainLayout)
        
        # UI
        '''
        self.button1 = QtWidgets.QPushButton('sadfds')
        self.button2 = QtWidgets.QPushButton('sadsfdsfdcxv')
        
        self.mainLayout.addWidget(self.button1)
        self.mainLayout.addWidget(self.button2)
        '''
        
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(390)
        self.scrollArea.setMaximumWidth(390)
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)
        
        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,0,0)
        self.scroll_layout.setSpacing(5) #layout
        
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.mainLayout.addWidget(self.scrollArea) #add to main layout
        
  
        # Separator
        self.separatorLine1 = QtWidgets.QFrame()
        self.separatorLine1.setFrameShape( QtWidgets.QFrame.HLine )
        
        self.mainLayout.addWidget(self.separatorLine1)
            
            
        # Buttons
        self.buttonFix = QtWidgets.QPushButton('Fix')
        self.buttonFix.setMinimumHeight(30)
        self.buttonFix.clicked.connect(self.runFix)
        self.buttonRun = QtWidgets.QPushButton('Run Check')
        self.buttonRun.setMinimumHeight(30)
        self.buttonRun.clicked.connect(self.runChecker)
        
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(3)
        self.buttonsLayout.addWidget(self.buttonFix)
        self.buttonsLayout.addWidget(self.buttonRun)
        
        self.mainLayout.addLayout(self.buttonsLayout)
        

def main():
    
    if cmds.workspaceControl('mySceneCheckerWorkspaceControl', exists=True):
        cmds.deleteUI('mySceneCheckerWorkspaceControl', control = True)
        cmds.workspaceControlState('mySceneCheckerWorkspaceControl', remove=1)
        
    myUI = SceneChecker()
    myUI.show(dockable = True, area='right', allowedArea='right', floating=True)
    
    cmds.workspaceControl('mySceneCheckerWorkspaceControl',
                            label = 'SceneChecker',
                            edit = 1,
                            tabToControl = ['AttributeEditor', -1],
                            widthProperty = 'fixed',
                            initialWidth = 400)
    
    
main()