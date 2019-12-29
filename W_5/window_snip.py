import maya.cmds as cmds

def main():
    
    if cmds.window("MyWindowID", exists = 1):
        cmds.deleteUI("MyWindowID")

       
    if cmds.windowPref("MyWindowID", exists = 1):
        cmds.windowPref("MyWindowID", remove = 1)  
    
    
    cmds.window('MyWindowID', title= "MyWindow", width= 400, height = 300 )
    
    
    cmds.showWindow("MyWindowID")