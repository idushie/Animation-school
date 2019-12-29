import maya.cmds as cmds
import maya.mel as mel

mainWindow = mel.eval('global string $gMainWindow; $a = $gMainWindow;')

newMenu = cmds.menu("myUniqueMenu", l="Test Menu", tearOff = True, p = mainWindow)

def runShit():
    print "shit"

item1 = cmds.menuItem(l="Run Some Tool", c = "runShit()", p = newMenu)


# delete menu

if cmds.menu("myUniqueMenu", exists=True):
    cmds.deleteUI("myUniqueMenu")