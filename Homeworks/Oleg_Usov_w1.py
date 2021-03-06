###########################################################
#Констрейн для одной руки
###########################################################
import maya.cmds as cmds

objects = cmds.ls(selection=1)

Locator1 = cmds.spaceLocator()    

parentHand = cmds.listRelatives(objects[0], parent = 1)
Parent1 = cmds.parent(Locator1,parentHand)

Match = cmds.matchTransform(Locator1,objects[0])

LocatorScale = cmds.scale( 0.1, 0.1, 0.1, Locator1)

Locator2 = cmds.spaceLocator()

WeaponGroup = cmds.group(objects[1], Locator2, n='Weapon_grp')

Match = cmds.matchTransform(Locator2,objects[1])

WeaponConst1 = cmds.parentConstraint(Locator2,objects[1])
WeaponConst2 = cmds.parentConstraint(Locator1,WeaponGroup, mo=1,)
###########################################################
#Домашка
###########################################################
import maya.cmds as cmds
Sphere = cmds.polySphere()
TimelineStart = cmds.playbackOptions(minTime=1)
TimelineEnd = cmds.playbackOptions(maxTime=120)
KeyStart = cmds.setKeyframe(Sphere, v = -10, at='translateX', t=TimelineStart) 
KeyEnd = cmds.setKeyframe(Sphere, v = 10, at='translateX', t=TimelineEnd)
Cube = cmds.polyCube()
MoveCube = cmds.move(-10,0,10,Cube)
ConstrCube = cmds.parentConstraint(Sphere, Cube, mo=1)
BakeCube = cmds.bakeResults(Cube,simulation=True, t=(TimelineStart,TimelineEnd))
ClearCube = cmds.delete(ConstrCube)