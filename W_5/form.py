import maya.cmds as cmds

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
    if ch_bx2:
         cmds.createDisplayLayer() 
# Window conditions       
if cmds.window('myWindow1', exists = 1):
    cmds.deleteUI(myWindow1, window = True)
    
if cmds.windowPref('myWindow1', exists = 1):
    cmds.windowPref('myWindow1', remove = 1)
 #Create window and show 
myWindow1 = cmds.window('myWindow1', title = 'Object creator', wh = (300, 230))
cmds.showWindow( 'myWindow1' )


#Form1
frm_1 = cmds.formLayout( )
#Txt field
txt_f = cmds.textField('txt_field', p = frm_1, pht = 'Object Name', h = 30 )
#Radio_btns
rdn_btns = cmds.radioButtonGrp('radio_btn_grp', p =frm_1, sl = 1, labelArray3=['Sphere', 'Cube', 'Cone'], 
                                                       numberOfRadioButtons=3, 
                                                  cal =[(1, 'left'), (2, 'center'), (3, 'right')])
#ch_boxes
ch_bx1 = cmds.checkBox('ch_bx1',p = frm_1, label='Put into a group', )
ch_bx2 = cmds.checkBox('ch_bx2',p = frm_1, label='Move x by 10 unit' )
ch_bx3 = cmds.checkBox('ch_bx3',p = frm_1, label='Display Layer/Template' )

#Buttons
create_btn = cmds.button(p = frm_1, label = 'Create', h = 30,  command = create_obj )
cancel_btn = cmds.button(p = frm_1, label = 'Cancel', h = 30,  command = 'cmds.deleteUI("myWindow1")')


cmds.formLayout(frm_1, e =1 , af = [(txt_f, 'left', 20),
                                   (txt_f, 'right',20),
                                   (txt_f, 'top', 5),
                                   (rdn_btns, 'right',20),
                                   (rdn_btns, 'left',20),
                                   (create_btn, 'left', 20),
                                    (create_btn, 'bottom', 10),
                                    (cancel_btn, 'right', 20),
                                    (cancel_btn, 'bottom', 10)],
                              ac = [(rdn_btns, 'top',20, txt_f),
                                    (ch_bx1, 'top',20, rdn_btns),
                                    (ch_bx2, 'top',5, ch_bx1),
                                    (ch_bx3, 'top',5, ch_bx2),
                                    (create_btn, 'top',20, ch_bx3),
                                    (cancel_btn, 'top',20, ch_bx3)],
                              ap = [(create_btn, 'right',5, 50),
                                    (cancel_btn, 'left',0, 50)])