import maya.cmds as cmds
import json

myPath = "C:/Users/Neron4ik/Documents/maya/projects/Programming/scripts/MyProject/test.json"

sph = cmds.ls(sl=1, l=0)[0]
tx = round(cmds.getAttr(sph+".tx"), 5)
ty = round(cmds.getAttr(sph+".ty"), 5)
tz = round(cmds.getAttr(sph+".tz"), 5)
rx = round(cmds.getAttr(sph+".rx"), 5)
ry = round(cmds.getAttr(sph+".ry"), 5)
rz = round(cmds.getAttr(sph+".rz"), 5)

a = {}
a[sph] = {"tx":tx, "ty":ty, "tz":tz, "rx":rx, "ry":ry, "rz":rz}
print a


with open(myPath, "w") as jFile:
    json.dump(a, jFile, indent = 4)