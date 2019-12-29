"""ColumnLayout
"""

myLayout  = cmds.columnLayout()
cmds.button(label = "text", parent = myLayout)
cmds.iconTextButton(label = "text", style="textOnly", w=30, h=30, parent = myLayout)

"""rowLayout
"""

frm = cmds.rowLayout( numberOfColumns = 4,
                      cl4 = ["right", "left", "center", "center"],
                      co4 = [0,0,100,0],
                      cw4=[100,50,50,50])

b1 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b1", parent = frm)
b2 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b2", parent = frm)
b3 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b3", parent = frm)
b4 = cmds.button(label="test", parent = frm)

"""formLayout
"""

frm = cmds.formLayout(w = 300, h = 200)

b1 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b1", parent = frm)
b2 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b2", parent = frm)
b3 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b3", parent = frm)
b4 = cmds.button(label="test", parent = frm)

cmds.formLayout(frm, edit=True, attachForm = [
                                 (b2, "left", 100)
                                ],
                                attachControl = [
                                 (b1, "left", 50, b2)
                                ],
                                attachPosition = [
                                 (b3, "left", -15, 50),
                                 (b3, "top", -15, 50)
                                ])

"""frameLayout
"""

clm = cmds.columnLayout()
frm = cmds.frameLayout( "testFrameLayoutA",
                        labelVisible = True,
                        collapse = 1,
                        label = "Test Shit",
                        w = 300,
                        collapsable=True,
                        borderVisible=False,
                        parent = clm)
b1 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b1", parent = frm)
b2 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b2", parent = frm)
b3 = cmds.iconTextButton(style='textOnly', w=30, h=30, label="b3", parent = frm)
b4 = cmds.button(label="test", parent = frm)