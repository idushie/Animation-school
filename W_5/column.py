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
    #Cmd show window
    cmds.showWindow("MyWindowID")
   
    #column - Vetical
    col = cmds.columnLayout('asdsa')
    cmds.button(parent = col)
    
    #row - Horizontal, always assign numberOfColumns 
    hor = cmds.rowLayout('Python', numberOfColumns = 4, cw4 = [100,50,50,50])
    cmds.button(width = 30)
    cmds.button(width = 30)
    cmds.button(width = 30)
    cmds.button(width = 30)
    
main()