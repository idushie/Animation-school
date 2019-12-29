import maya.cmds as cmds

def applyExpression(expField = None):

    selectedObjects = cmds.ls(sl=1,l=1)

    exp = cmds.textField(expField, q=1, text=1)

    if "*" in exp:

        for i in selectedObjects:

            objectName = i.split("|")[-1]

            newname = exp.replace("*", objectName)

            cmds.rename(i, newname)

        cmds.textField(expField, e=1, text="")


def main():


    if cmds.window("MyWindow", exists = 1):
        cmds.deleteUI("MyWindow")

    if cmds.windowPref("MyWindow", exists = 1):
        cmds.windowPref("MyWindow", remove = 1)

    #creates window but leaves it invisible
    cmds.window("MyWindow", title="Object Renamer v1.0", width = 250, tlb = 1)

    mainLayout = cmds.columnLayout( adjustableColumn = True,
                                    rowSpacing = 15)

    # Expression
    expressionlayout  = cmds.columnLayout(  adjustableColumn = True,
                                    columnAlign = "left",
                                    columnOffset = ["both", 10],
                                    rowSpacing = 5,
                                    statusBarMessage = "Use * as an actual name",
                                    parent = mainLayout)

    cmds.text("Expression:", parent = expressionlayout)
    expField = cmds.textField(placeholderText = "*", parent = expressionlayout)

    # Object Names List
    scrollL = cmds.scrollLayout(childResizable=1, parent = mainLayout)
    colL = cmds.columnLayout(parent=scrollL, adj=1, rowSpacing=1, columnOffset = ["both", 10])


    selectedObjects = cmds.ls(sl=1, l=1)

    # for each selected object - create nameField
    for i in selectedObjects:
        name = i.split("|")[-1]
        cmds.nameField(o = i)


    #add buttons
    buttonsLayout = cmds.columnLayout(parent = mainLayout, rowSpacing = 3, adj = 1)
    cmds.button(label="Apply", c =  "applyExpression(expField = '{}')".format(expField), parent = buttonsLayout)
    cmds.button(label="Close", c = "cmds.deleteUI(\"MyWindow\")", parent = buttonsLayout)

    #show the actual window
    cmds.showWindow("MyWindow")


main()