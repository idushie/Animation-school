import maya.cmds as cmds
from random import randint, choice

list_objects = cmds.listRelatives('objects')

list_locators = cmds.ls(type = 'locator')
locators_transform = cmds.listRelatives(list_locators, p=1, f=1)


def exchange(objects=list_objects, locators=locators_transform):

    index = [0,1,2]

    for locator in locators_transform:
        
        #* Create not repeating number 
        random_index = randint(index[0],index[len(index)-1])
        index.remove(random_index)
        
        object = list_objects[random_index]
        
        cmds.matchTransform(object, locator )
        locator_group = cmds.listRelatives(locator, p=1)
        
        if locator_group:
            cmds.parent(object, locator_group)
        else:
            cmds.parent(object, w=True)
            
        cmds.delete(locator)

exchange()