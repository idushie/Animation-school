import maya.cmds as cmds
import maya.mel as mel

# this global var contains the full path to be layout, where all buttons are located
toolbox = mel.eval('global string $gToolBox; $a = $gToolBox;')
print toolbox  #out:   ToolBox|MainToolboxLayout|frameLayout5|flowLayout6

# this global var contains the name of the main toolbox layout
# (In case if we want to add some other elements to it)
toolBoxForm = mel.eval('global string $gToolboxForm; $a = $gToolboxForm;')
print toolBoxForm  #out: MainToolboxLayout

cmds.setParent(toolbox) #set parent to the flowLayout6

def test():
  print "Hello World"

cmds.gridLayout('myTestLayout', numberOfColumns = 1, width = 36, cellWidthHeight = [36,36])
cmds.setParent('myTestLayout')

cmds.button(c ="test()")

cmds.popupMenu()
cmds.menuItem(l='test One', c = "test()")
cmds.menuItem(l='test Two', c = "test()")
cmds.menuItem(l='test Three', c = "test()")
#we can also use toolButton instead of a regular button

#prints all the toolbox layout children
print cmds.flowLayout(toolbox, q=1, childArray = 1)

#if we want to delete layout - just run this command
cmds.deleteUI('myTestLayout')