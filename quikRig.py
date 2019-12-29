import maya.cmds as cmds

def lockKeyableAttrs(obj, animControl):
    """
    Lock all keyable attributes (displayed in Channel Box)
    [attr] $object - gives this function an object to delete all keyable attributes from it 
    [attr] $animControl - if true, keeps translate and rotate attributes unlocked and keyable
    """
    
    #get all keyable attributes. 
    #listAttr returns array of strings
    keyable_attrs = cmds.listAttr(obj, k=True)

    for attr in keyable_attrs:


        if animControl and ("rotate" in attr or "translate" in attr):
            continue


        cmds.setAttr(obj + "." + attr, k=False)

        if attr == "visibility":
            continue


        cmds.setAttr(obj + "." + attr, lock=True)




def createMasterNodes():
    """
    Create basic scene hierarchy |scene_master|prop_master
    prop_master - is a group where all our rigs will be parented
    """

    #if "scene_master" group doesn't exists in our Maya scene ( ! means NOT )
    if not cmds.objExists("scene_master"):

        #create group and lock it's attributes
        scene_master = cmds.group(n="scene_master", em=True)
        lockKeyableAttrs(scene_master, 0)


    if not cmds.objExists("prop_master"):
        prop_master = cmds.group(n="prop_master", em=True, p="scene_master")
        lockKeyableAttrs(prop_master, 0)




def createRigDisplayLayer(rig):
    """
    Creates a Display Layer and adds $rig to this layer
    [attr] $rig - current rig which we pass in to this function
    """

    layerName = rig + "_DL"

    cmds.createDisplayLayer(name=layerName) #create a layer

    cmds.editDisplayLayerMembers(layerName, rig) #add a rig to it



def createRig(optLayer = 0, optScene = 0):






    # get selected objects names
    selectedObjects = cmds.ls(selection=1)

    # here we create rig for each selected object
    # obj in this loop is a current object taken from array selectedObjects
    for obj in selectedObjects:

        # create obj_base_rig group
        base_rig = None

        if(optScene):

            # create main scene groups
            createMasterNodes()

            # parent the rig group to prop_master group
            base_rig = cmds.group(name = obj + "_base_rig", empty=True, p="prop_master")

        else:

            # create a new group parented to World
            base_rig = cmds.group(name = obj + "_base_rig", empty=True)


        # Create a display layer and add the rig to taht layer
        if optLayer:
            createRigDisplayLayer(base_rig)

        
        
        # RIG HIERARCHY

        # create an empty group
        grp_base_model = cmds.group(name=obj + "_base_model", empty=True, parent=base_rig)
        lockKeyableAttrs(grp_base_model, 0)

        grp_base_motion = cmds.group(name=obj + "_base_motion", empty=True, parent=base_rig)
        lockKeyableAttrs(grp_base_motion, 0)

        grp_base_vis = cmds.group(name=obj + "_base_visibility", empty=True ,parent=grp_base_motion)
        lockKeyableAttrs(grp_base_vis, 0)

        grp_scene_offset = cmds.group(name=obj + "_scene_offset", empty=True, parent=grp_base_motion)
        lockKeyableAttrs(grp_scene_offset, 0)

        # create a NURBS curve controller
        crv_ac_master = cmds.curve(d=1, p = [(-3,0,-1.5),(3,0,-1.5),(0,0,4),(-3,0,-1.5)], n=obj + "_ac_master")
        cmds.parent(crv_ac_master, grp_scene_offset)
        
        grp_ac_master_offset = cmds.group(name=obj + "_ac_master_offset" ,empty=True ,parent=crv_ac_master)
        lockKeyableAttrs(grp_ac_master_offset, 1)

        crv_ac_pivot = cmds.curve(d=1, p = [(0,0,2),(0,0,-2),(0,0,0),(-2,0,0),(2,0,0),(0,0,0),(0,2,0),(0,-2,0)], n=obj + "_ac_pivot")
        cmds.parent(crv_ac_pivot, grp_ac_master_offset)
        lockKeyableAttrs(crv_ac_pivot, 1)

        grp_ac_pivot_neg = cmds.group(name=obj + "_ac_pivot_neg", empty=True, parent=crv_ac_pivot)
        
        grp_ac_cog_attr = cmds.group(name=obj + "_ac_cog_attr", empty=True, parent=grp_ac_pivot_neg)
        lockKeyableAttrs(grp_ac_cog_attr, 0)

        crv_ac_cog = cmds.curve(d=1, p=[(-2,0,-1),(2,0,-1),(0,0,3),(-2,0,-1)], n=obj + "_ac_cog")
        cmds.parent(crv_ac_cog, grp_ac_cog_attr)
        lockKeyableAttrs(crv_ac_cog, 1)
        
        grp_ac_cog_offset = cmds.group(name=obj + "_ac_cog_attr", empty=True, parent=crv_ac_cog)
        lockKeyableAttrs(grp_ac_cog_offset, 1)


        # apply object transformations to the rig body controller
        # save object transforms
        obj_translate = cmds.getAttr(obj + ".translate")[0]
        obj_rotate = cmds.getAttr(obj + ".rotate")[0]

        # zero out object translate
        cmds.setAttr(obj + ".translate", 0,0,0)
        cmds.setAttr(obj + ".rotate", 0,0,0)


        # RESCALE CONTROLLERS
        # Large objects should have larger controllers, small objects - smaller controllers
        # But the main idea is that controllers should be visible and surround the object

        # get current object bounding box information
        objectBB = cmds.xform(obj, q=1, ws=1, bb=1)
        # get master curve controller bounding box information
        masterCurveBB = cmds.xform(crv_ac_master, q=1, ws=1, bb=1)

        # calculate Z-Length of those objects
        objectBB_zLength = objectBB[5] - objectBB[2]
        masterCurveBB_zLength = masterCurveBB[5] - masterCurveBB[2]

        # Find the coefficient for scaling controllers
        coeff = (objectBB_zLength / masterCurveBB_zLength) * 2

        # scale curve master (it will also scale all the child controllers)
        cmds.scale(coeff, coeff, coeff, crv_ac_master, r=1)

        # master controller - lock attributes
        lockKeyableAttrs(crv_ac_master, 1)


        # PLACE THE OBJECT UNDER THE RIG

        # parent the object to the rig_base_model group
        cmds.parent(obj, grp_base_model)

        # apply parent constraint so the rig_ac_cog_offset group could influence the object's translation and rotation
        cmds.parentConstraint(grp_ac_cog_offset, obj, maintainOffset = 1)

        # return master controller to the place where the object has been moved and rotated initially
        cmds.setAttr(crv_ac_master + ".translate", obj_translate[0], obj_translate[1], obj_translate[2])
        cmds.setAttr(crv_ac_master + ".rotate", obj_rotate[0], obj_rotate[1], obj_rotate[2])


        # OBJECT VISIBILITY
        # Adds an enum attribute with options "Off : On : Body" to  master controller
        # The idea is:
        #   Off - rig is visible, object is hidden
        #   On - rig is visible, object is visible but unselectable
        #   Edit - rig is visible, object is visible and selectable
        
        # add enum attr "body" to master controller and rig_base_visibility group
        cmds.addAttr(crv_ac_master, ln="body", at="enum", en="off:on:edit", k=1)
        cmds.addAttr(grp_base_vis, ln="body", at="enum", en="off:on:edit", k=1)

        # set initial attr value = On (rig is visible, object is visible but unselectable)
        cmds.setAttr(crv_ac_master + ".body", 1)
        cmds.setAttr(grp_base_vis + ".body", 1)

        # Connect "body" attr of master controller and "body" attr of the visibility group
        cmds.connectAttr(crv_ac_master + ".body", grp_base_vis + ".body", f=1)

        # create utility nodes (with some initial values) that will give us the way
        #   to control object's visibility and select mode by our enum attribute
        visibilityUtilMDL = cmds.shadingNode("multDoubleLinear", asUtility=1, n = obj + "_base_visibility_mdl")
        cmds.setAttr(visibilityUtilMDL + ".input1", 1)

        visibilityUtilCND = cmds.shadingNode("condition", asUtility=1, n = obj + "_base_visibility_cnd")
        cmds.setAttr(visibilityUtilCND + ".colorIfFalseR", 2)
        cmds.setAttr(visibilityUtilCND + ".secondTerm", 2)

        # connect the visibility group attr "body" with utility nodes
        cmds.connectAttr(grp_base_vis + ".body", visibilityUtilMDL + ".input2", f=1)
        cmds.connectAttr(grp_base_vis + ".body", visibilityUtilCND + ".firstTerm", f=1)

        # connect the utility nodes with the rig_base_model group attributes
        cmds.connectAttr(visibilityUtilMDL + ".output", grp_base_model + ".overrideEnabled", f=1)
        cmds.connectAttr(visibilityUtilMDL + ".output", grp_base_model + ".visibility", f=1)
        cmds.connectAttr(visibilityUtilCND + ".outColorR", grp_base_model + ".overrideDisplayType", f=1)



        # ROTATION PIVOT
        # It should rotate the offset controller around it - but not translate it
        # When we move controller - the negative translate values should be applied to the child group

        # create the utility node multiplyDivide
        pivot_MD = cmds.shadingNode("multiplyDivide", asUtility=1, n = obj + "_pivot_neg_multdiv")
        cmds.setAttr(pivot_MD + ".input2X", -1)
        cmds.setAttr(pivot_MD + ".input2Y", -1)
        cmds.setAttr(pivot_MD + ".input2Z", -1)

        # make connections 
        cmds.connectAttr(crv_ac_pivot + ".translateX", pivot_MD + ".input1X", f=1)
        cmds.connectAttr(crv_ac_pivot + ".translateY", pivot_MD + ".input1Y", f=1)
        cmds.connectAttr(crv_ac_pivot + ".translateZ", pivot_MD + ".input1Z", f=1)

        cmds.connectAttr(pivot_MD + ".outputX", grp_ac_pivot_neg + ".translateX", f=1)
        cmds.connectAttr(pivot_MD + ".outputY", grp_ac_pivot_neg + ".translateY", f=1)
        cmds.connectAttr(pivot_MD + ".outputZ", grp_ac_pivot_neg + ".translateZ", f=1)
        lockKeyableAttrs(grp_ac_pivot_neg, 0)

        # final strokes
        cmds.select(d=1)




        


createRig(optLayer = 1, optScene = 1)