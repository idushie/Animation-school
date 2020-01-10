import maya.cmds as cmds

#скрипт для задания 1
#-------------------------------
cmds.aimConstraint( 'pSphere1','pSphere2',u = [0,0,1], wut = "object", wuo = "locator1"  )
#скрипт для задания 2
#-------------------------------
if "rotateOrder" in cmds.listAttr():
    print (list_attr)
#скрипт для задания 3
#-------------------------------
if cmds.getAttr('pSphere1.translateX') < 0:
    cmds.move(0, x = 1)
if cmds.getAttr('pSphere1.translateY') < 0:
    cmds.move(0, y = 1)
if cmds.getAttr('pSphere1.translateZ') < 0:
    cmds.move(0, z = 1)
#скрипт для задания 4
#-------------------------------
list_objects = cmds.ls(type ="locator" )
#скрипт для задания 5
#-------------------------------
def attr_value(obj,attribute = 0):
    if attribute == 0:
        return 0
    else:    
        value = cmds.getAttr(obj+"."+attribute)
    return value

#скрипт для задания 6
#-------------------------------
import maya.cmds as cmds
list_all = []
list_locators = cmds.ls(type ="locator" )
list_nurbs = cmds.ls(type ="nurbsCurve" )
for i in list_locators:
    list_all.append (i)
for x in list_nurbs:
    list_all.append (x)
print list_all
#скрипт для задания 7
#-------------------------------
list_child = cmds.listRelatives(f = 1, c = 1, ad = 1)