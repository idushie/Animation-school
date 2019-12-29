import maya.cmds as cmds

#Function create sphere
def createSphere():
    n = cmds.textField('tfieldID', q=1, text = 1)    

    cmds.polySphere(name = n)
#Chek if window with this ID alredy exisits , delete it 
def main():
    
    if cmds.window("MyWindowID", exists = 1):
        cmds.deleteUI("MyWindowID")

    #Chek if window prefernces alredy changed, delete it     
    if cmds.windowPref("MyWindowID", exists = 1):
        cmds.windowPref("MyWindowID", remove = 1)  

    #Создание окна(в пямяти), имя онка(ID), отображаемое имя, параметры
    cmds.window('MyWindowID', title= "MyWindow", width= 400, height = 300 )

    #Create columnLayout
    col = cmds.columnLayout('myColumnLayout')
    #Create button with id, name, parent = Layout, 
    cmds.button('btn01_id', label = "Sphere", parent = col, command = "createSphere()", statusBarMessage = "Click this button", width = 200)
    cmds.textField("tfieldID", parent = 'myColumnLayout', width = 200, height = 30, placeholderText = "Sphere Name")

    #Cmd show window
    cmds.showWindow("MyWindowID")

main()