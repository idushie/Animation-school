import maya.cmds as cmds
from random import randint, choice


def snap_to_object():

    '''Target object selected last '''

    list_all = cmds.ls(sl=1)
    target_object = list_all[-1]

    vertex_count = cmds.polyEvaluate(target_object, v=True)

    list_objects = list_all[:-1]

    for object in list_objects:

        random_vertex = randint(0,vertex_count)
        
        x,y,z = cmds.pointPosition(target_object + '.vtx[' + str(random_vertex) + ']')
        
        cmds.move(x,y,z, object)

