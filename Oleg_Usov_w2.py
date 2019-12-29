import maya.cmds as cmds
def CleanZeroKeys (All=True, Clean=True):
#Create empty list
    List_curvs =[]
# Function argument condition
    if All==True:
# IF TRUE: List ALL obj in scene and put in list only nurbs with "_cn_"
        AllCurvs = cmds.ls('*_cn_*',l=1,)
        for i in AllCurvs:
            CurvsShape = cmds.listRelatives(i, c=1, f=1)
            Type = cmds.nodeType(CurvsShape)
            if Type == "nurbsCurve":
                List_curvs.append(i)
    else:
#IF FALSE: List selected obj and put in list only  nurbs with "_cn_"
        SlCurvs = cmds.ls('*_cn_*',sl=1,l=1,)
        for i in SlCurvs:
            CurvsShape = cmds.listRelatives(i, c=1, f=1)
            Type = cmds.nodeType(CurvsShape)
            if Type == "nurbsCurve":
                List_curvs.append(i)
#Function argument condition 
    if Clean:
#IF TRUE: clean zero keys 
        for Curv in List_curvs:
            for Attr in (cmds.listAttr(Curv, k=1)):
                KeyCount = cmds.keyframe(Curv + '.' + Attr, q=1, kc=1)
                if KeyCount >= 1:
                    Keys = cmds.keyframe( Curv + '.' + Attr, query=1, valueChange=1)
                    SetKeys = set(Keys)
                    KeysLen = len(SetKeys)
                    if KeysLen == 1:
                        cmds.delete(Curv + '.' + Attr, c=True )
    else:
#IF FALSE: put curvs in list
        return (List_curvs)   