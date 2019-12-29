import maya.cmds as cmds

import maya.mel as mel


mainWindow = mel.eval('global string $gMainWindow; $a = $gMainWindow;')

newMenu = cmds.menu("myUniqueMenu", l="Animation school", tearOff = True, p = mainWindow)

item1 = cmds.menuItem(l="Object creator", c = "mainUI()", p = newMenu)

def create_obj(*args): 
    radio_btn = cmds.radioButtonGrp('radio_btn_grp', q = True, sl = True)
    name_obj = cmds.textField('txt_field',q = 1, tx = True)
    ch_bx1 = cmds.checkBox('ch_bx1', q = True, v = True)
    ch_bx2 = cmds.checkBox('ch_bx2', q = True, v = True)
    ch_bx3 = cmds.checkBox('ch_bx3', q = True, v = True)
    # Radio btn`s conditions
    if radio_btn == 1:   
        cmds.polySphere(n = name_obj)
    elif radio_btn == 2:
        cmds.polyCube(n = name_obj)
    else:
        cmds.polyCone(n = name_obj)
    # Check box`s conditions   
    if ch_bx1:
        cmds.group (n = name_obj +'_grp')
    if ch_bx2:
        cmds.setAttr ('.tx', 10)
    if ch_bx3:
         layer = cmds.createDisplayLayer()
         cmds.setAttr("{}.displayType".format(layer),1) 

def run():
    cmds.polySphere() 


def mainUI():
    
    # Window conditions       
    if cmds.window('myWindow1', exists = 1):
        cmds.deleteUI(myWindow1, window = True)
        
    if cmds.windowPref('myWindow1', exists = 1):
        cmds.windowPref('myWindow1', remove = 1)
    
    #Create window and show 
    myWindow1 = cmds.window('myWindow1', title = 'Object creator', wh = (300, 230))
    cmds.showWindow( 'myWindow1' )
    
    #Main col
    col_main = cmds.columnLayout('mainLayout', adj = True, co = ('both', 10), rowSpacing = 20)
    
    #Row 1 and textFild
    row_1 = cmds.rowLayout('row_1',adj = True, parent = 'mainLayout')
    cmds.textField('txt_field', p = 'row_1', pht = 'Object Name', h = 30 )
    
    #Row 2 and radioButtons
    row_2 = cmds.rowLayout('row_2',adj = True, parent = 'mainLayout')
    cmds.radioButtonGrp('radio_btn_grp', p ='row_2',sl = 1, labelArray3=['Sphere', 'Cube', 'Cone'], numberOfRadioButtons=3, cal =[(1, 'left'), (2, 'center'), (3, 'right')])
    
    #Col 1 and CheckBoxes
    col_1 = cmds.columnLayout('col_1',p ='mainLayout', adj = True, rowSpacing = 10)
    cmds.checkBox('ch_bx1',p = 'col_1', label='Put into a group', )
    cmds.checkBox('ch_bx2',p = 'col_1', label='Move x by 10 unit' )
    cmds.checkBox('ch_bx3',p = 'col_1', label='Display Layer/Template' )
    
    #Form 1 and buttons
    form_1 = cmds.formLayout(parent = 'mainLayout')
    create_btn = cmds.button(p = form_1, label = 'Create', h = 30,  command = create_obj )
    cancel_btn = cmds.button(p = form_1, label = 'Cancel', h = 30,  command = 'cmds.deleteUI("myWindow1")')
    
    cmds.formLayout (form_1, e = 1, af = [(create_btn, 'left', 0),
                                          (create_btn, 'bottom', 10),
                                          (create_btn, 'top', 0),
                                          (cancel_btn, 'right', 0),
                                          (cancel_btn, 'bottom', 10),
                                          (cancel_btn, 'top', 0)],
                                    ap = [(create_btn, 'right',5, 50),
                                          (cancel_btn, 'left', 0, 50)])


