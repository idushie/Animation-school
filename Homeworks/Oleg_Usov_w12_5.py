'''Имеется некая геометрическая поверхность в сцене. Вам необходимо написать скрипт,
 который расположит другие выделенные объекты (сферы или локаторы, неважно) 
 на поверхности текущего объекта в рандомных позициях. 
 Используйте любой известный вам метод.'''

import maya.cmds as cmds
from random import randint

list_all = cmds.ls(sl=1)
vertex_count = cmds.polyEvaluate(list_all[-1], v=True)


list_objects = list_all[:len(list_all)-1]

for object in list_objects:

    random_vertex = randint(0,vertex_count)
    
    x,y,z = cmds.pointPosition(list_all[-1]+'.vtx['+ str(random_vertex) +']')
    
    cmds.move(x,y,z, object)

