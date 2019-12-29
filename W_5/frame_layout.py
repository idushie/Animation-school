import maya.cmds as cmds

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

    # Frame
    frm = cmds.frameLayout('layoutID',collapse = 1, label = 'Yo ma', collapsable = 1, borderVisible = 0)

    scrl = cmds.scrollLayout(horizontalScrollBarThickness = 16, verticalScrollBarThickness = 16)

    cmds.columnLayout()

    A1 = cmds.button( )
    A2 = cmds.button()
    A3 = cmds.button()
    A4 = cmds.button() 
    A5 = cmds.button()
    A6 = cmds.button()