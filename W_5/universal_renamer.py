import maya.cmds as cmds
def applyExression():

    selectedObj = cmds.ls(sl=1, l = 1)
    
    exp = cmds.textField('expressionFieldID', q = 1, text = 1)
    
    if '*' in exp:

        for i in selectedObj:

            objname = i.split('|')[-1]

            newName = exp.replace('*', objname)

            cmds.rename(i, newName)

    cmds.textField('expressionFieldID', e = 1, text = '')




def main():
    if cmds.window('MyWindow', exists = 1):
        cmds.deleteUI('MyWindow')
    
    if cmds.windowPref('MyWindow', exists = 1):
        cmds.windowPref('MyWindow', remove = 1)
    
    cmds.window('MyWindow', title = 'Universal Renamer 1.0', w = 250, h = 300)
    
    #--------------------------
    
    #--------------------------
    
    cmds.showWindow('MyWindow')

    mainLayout = cmds.columnLayout(adj = True, rowSpacing = 15)

    #Expression

    expressionLayout = cmds.columnLayout(adj = True,
                                         columnAlign = 'left', 
                                         co = ['both',10],
                                         rowSpacing = 5,
                                         statusBarMessage = 'Use * as an actual name',
                                         parent = mainLayout)
    cmds.text('Expression:', parent = expressionLayout)
    expField = cmds.textField('expressionFieldID', placeholderText = '*', parent = expressionLayout)

    # Objects name list
    
    scrollL = cmds.scrollLayout('scrollLayoutID',  childResizable = 1, parent = mainLayout)
    colL = cmds.columnLayout(parent = scrollL, adj = True, rowSpacing = 1, co = ['both', 10])
    
    selectedObj = cmds.ls(sl=1, l = 1)
    
    for i in selectedObj:
        #name = i.split('|')[-1]
        cmds.nameField(o = i)
    # Buttons
    buttonLayout = cmds.columnLayout(parent = mainLayout, rowSpacing = 3, adj = 1)
    cmds.button(label = 'Apply', command = 'applyExression()', parent = buttonLayout)
    cmds.button(label = 'Cancel', command = 'cmds.deleteUI("MyWindow")', parent = buttonLayout)
    #-----------------------------------


main()