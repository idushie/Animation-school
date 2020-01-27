import maya.cmds as cmds
from random import randint

list_objects = cmds.listRelatives('objects')

list_locators = cmds.ls(type = 'locator')
locators_transform = cmds.listRelatives(list_locators, p=1, f=1)

numbers = [0,1,2]

for locator in locators_transform:
    
	#* Create not repeating number 
    random_number = randint(numbers[0],numbers[len(numbers)-1])
    numbers.remove(random_number)
	
    object = list_objects[random_number]
    
    cmds.matchTransform(object, locator )
    locator_group = cmds.listRelatives(locator, p=1)
    
    if locator_group:
        cmds.parent(object, locator_group)
    else:
        cmds.parent(object, w=True)
        
    cmds.delete(locator)