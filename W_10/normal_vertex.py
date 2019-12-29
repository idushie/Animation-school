import maya.cmds as cmds
import random
import maya.OpenMaya as OpenMaya


selected_mesh = cmds.ls(sl=1, l=1)[0]

sel_list = OpenMaya.MSelectionList()

sel_list.add(selected_mesh)

dp = OpenMaya.MDagPath()
sel_list.getDagPath(0, dp)

it = OpenMaya.MItMeshVertex(dp)

while not it.isDone(): #* idDone -> bool

    normalVector = OpenMaya.MVector()
    
    it.getNormal(normalVector, OpenMaya.MSpace.kWorld)
    
    normalVector.normalize()

    pos = it.position(OpenMaya.MSpace.kWorld)

    new_pos = pos + normalVector * random.uniform(-1.0 , 1.0)

    it.setPosition(new_pos, OpenMaya.MSpace.kWorld)

    it.next() 
