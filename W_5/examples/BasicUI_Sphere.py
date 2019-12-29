import maya.cmds as cmds

# delete "MyWindow" if exists already
if cmds.window("MyWindow", exists = 1):
    cmds.deleteUI("MyWindow")
    
# delete "MyWindow"  prefs if exists 
if cmds.windowPref("MyWindow", exists = 1):
    cmds.windowPref("MyWindow", remove = 1)

#creates window but leaves it invisible
cmds.window("MyWindow", title="MyWnd", width = 400, height = 300, tlb = 1)

#show the actual window
cmds.showWindow("MyWindow")

myLayout  = cmds.columnLayout()

def createSphere():
    print "PolySphere has been created"
    cmds.polySphere()

button = cmds.button("btn01_id", label = "Sphere", parent = myLayout, command = "createSphere()", statusBarMessage = "Hello")
