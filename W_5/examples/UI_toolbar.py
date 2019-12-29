import maya.cmds as cmds

if cmds.window("myTestWindow", exists=1):
    cmds.deleteUI("myTestWindow")

if cmds.windowPref("myTestWindow", exists=1):
    cmds.windowPref("myTestWindow", remove=True)

if cmds.toolBar("myTestToolbar", exists = 1):
    cmds.deleteUI("myTestToolbar")

if cmds.windowPref("myTestToolbar", exists=1):
    cmds.windowPref("myTestToolbar", remove=True)

#this window will be used as a content for our toolbar
contentWindow = cmds.window("myTestWindow", sizeable = True)

#Main toolbar layout
mainFLayout = cmds.formLayout("mainFormLayoutSS")

#Toolbar
cmds.toolBar("myTestToolbar", area="bottom", content = contentWindow, allowedArea = ['bottom'])

#Some Custom Function
def test(x = ""):
    print x

# Create Right rowLayout with buttons
ff = cmds.rowLayout(numberOfColumns = 10, parent = mainFLayout, h=37)
cmds.iconTextButton(style="textOnly", w=50, h=30, command = test, label="Button B")
cmds.popupMenu()
cmds.menuItem(label = "Run Some Command", command = lambda *args: test())
cmds.menuItem(label = "Toggle Checkbox", checkBox = 1, c = lambda x: test(x))

#Edit formLayout to position the rowLayout
cmds.formLayout(mainFLayout, e=1, attachForm = [(ff, "right", 10)])

# Create LEFT rowLayout with buttons
dd = cmds.rowLayout(numberOfColumns = 10, parent = mainFLayout, h=37)
cmds.iconTextButton(style="textOnly", w=50, h=30, command = test, label="Button A")
cmds.popupMenu()
cmds.menuItem(label = "Run Some Command", command = lambda *args: test())
cmds.menuItem(label = "Run Another Command", command = lambda *args: test())
cmds.menuItem(label = "Run something else", command = lambda *args: test())
cmds.menuItem(label = "Toggle Checkbox", checkBox = 1, c = lambda x: test(x))

cmds.formLayout(mainFLayout, e=1, attachForm = [(ff, "right", 10), (dd, "left", 10)])