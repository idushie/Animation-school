import maya.cmds as cmds
import maya.OpenMaya as OpenMaya


selected_mesh = cmds.ls(sl=1, l=1)[0]

sel_list = OpenMaya.MSelectionList()

sel_list.add(selected_mesh)

dp = OpenMaya.MDagPath()
sel_list.getDagPath(0, dp)

it = OpenMaya.MItMeshEdge(dp)

while not it.isDone():
   
    p1 = it.point(0, OpenMaya.MSpace.kWorld)
    p2 = it.point(1, OpenMaya.MSpace.kWorld)
    c = it.center(OpenMaya.MSpace.kWorld)

    #*Curve degree = 2, requires 3 points
    curve = cmds.curve( p=[(p1.x, p1.y, p1.z), 
                           (c.x, c.y, c.z),
                           (p2.x, p2.y, p2.z)], d = 2)

    #*nr - normal vector of circle is difference between first point and second point
    circle = cmds.circle(nr= (p2.x-p1.x, p1.y-p2.y, p1.z-p2.z), 
                    c=(p1.x, p1.y, p1.z), r = 0.05 )
    
    cmds.extrude(circle[0], curve,  et=2 )
    

    it.next()


