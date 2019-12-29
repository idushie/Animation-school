import maya.cmds as cmds

def myLayout():
    cmds.columnLayout()
    cmds.button()
    cmds.button()
    cmds.button()

if cmds.workspaceControl("myuiWorkspaceControl", exists=True):
    cmds.deleteUI("myuiWorkspaceControl", control=True)
    cmds.workspaceControlState("myuiWorkspaceControl", remove=1)

#create workspace UI under AE tab
#Use {name}WorkspaceControl as a name
cmds.workspaceControl(  "myuiWorkspaceControl",                 #tab unique name
                        label="Borsch",                         #tab label
                        r=1,                                    #make tab active and focused
                        tabToControl=["AttributeEditor", -1],   #add tab next to AE
                        initialWidth=465,
                        minimumWidth=True,
                        widthProperty="preferred",
                        uiScript = "myLayout()")                #the script that builds UI