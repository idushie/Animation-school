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

button = cmds.button("btn01_id", label = "Sphere", parent = myLayout, command = "createSphere()", statusBarMessage = "Hello", width = 200)
textField = cmds.textField("textfld01_id", parent = myLayout, width = 200, placeholderText = 'Sphere Name')

def createSphere():
    n = cmds.textField("textfld01_id", q=1, text=1) # get "text" attribute value
    cmds.polySphere(name = n)