import maya.cmds as cmds
from time import sleep




class Carrier_rocket(Rocket):

    def __init__(self, height = 40., radius = 2., nozzle_count = 4, rocket_stage = 3):

        super(Carrier_rocket, self).__init__(height = height, radius = radius)

        self.nozzle_count = nozzle_count
        self.rocket_stage = rocket_stage
    
    
    def create_stage(self):
        
        stage = cmds.polyCylinder(r = self.rocket_radius, h = self.rocket_height, sh = self.rocket_stage)
        self.stage_shape = cmds.listRelatives(stage[0], c =1 , f =1 )
        cmds.setAttr ('.ty', self.rocket_height/2)

    
    def create_nozzle(self):
        list_nozzle = []
        height_nozzle = self.rocket_height/2
        
        if self.nozzle_count <= 20:
            for i in range(self.nozzle_count): 
                nozzle = cmds.polyCone(h = height_nozzle, r = self.rocket_radius / 1.3)
                list_nozzle.append(nozzle[0])
                
            list_vert = [24,34,29,39,26,36,31,22,27,32,25,35,23,33,37,21,20,30,28,38]
            
            for vert,nozzle in enumerate(list_nozzle):
                if self.rocket_stage <= 3:
                    x,y,z = cmds.pointPosition(self.stage_shape[0]+'.vtx[' +str(list_vert[vert])+']') 
                    cmds.move(x,height_nozzle/2,z,[nozzle])
                else:
                    x,y,z = cmds.pointPosition(self.stage_shape[0]+'.vtx[' +str(list_vert[vert]+(((self.rocket_stage/2)-1)*20))+']')
                    cmds.move(x,y - height_nozzle/2,z,[nozzle])
        else: 
            raise Exception('Too many nozzle, max nozzle is 20')

    def create_cabin(self):
        
        height_cabin = self.rocket_radius*2
        cmds.polyCone(r = self.rocket_radius, h = height_cabin )
        cmds.move(0,self.rocket_height + height_cabin/2,0)

class Rocket(object):

    def __init__(self, height = None, radius = None):
        self.rocket_height = float (height)
        self.rocket_radius = float (radius)
    

    def rocket_launch(self, time = 10):

        print ('До запуска ракеты:')
        for i in range(1,time+1):
            print (i)
            sleep(1)
        
        print self.flight()

    def flight(self):
        return 'Поехали!'   
class Missle(Rocket):

    def __init__(self, height = 10., radius = 1., ):

        super(Missle,self).__init__(height = height, radius = radius)

    def create_boudy(self):

        self.missle_grp = cmds.group(em = 1, n = 'Missle')
        self.missle_transf = cmds.polyCylinder(h = self.rocket_height, r = self.rocket_radius, ax = (0,0,1))[0]
        cmds.parent(self.missle_transf, self.missle_grp)

    
    def create_target(self):
        
        aim = cmds.circle( nr=(0, 0, 1), c=(0, 0, 0) )
        cmds.move(0,0,5+self.rocket_height)
        cmds.aimConstraint( aim[0], self.missle_grp, aim = (0,0,1) )


    def create_fuse(self):
        
        fuse_transf = cmds.polyCone(h = self.rocket_height/2, ax = (0,0,1), r = self.rocket_radius)[0]
        cmds.move(0, 0, self.rocket_height/2 + self.rocket_height / 4, fuse_transf)
        cmds.parent(fuse_transf, self.missle_grp)

    def create_wings(self):
        
        wing_length =  self.rocket_height / 2
        list_wings = []
        for i in range(4):
            wing_transf = cmds.polyCube(w = 0.2)[0]
            
            cmds.select(wing_transf + '.vtx[0:3]')
            cmds.move(wing_length, r =1, ls = 1, wd = 1, z = 1)
            
            cmds.select(wing_transf + '.vtx[4:5]')
            cmds.move(self.rocket_radius, y = 1, r = 1 )
            
            cmds.parent(wing_transf, self.missle_grp)
            list_wings.append(wing_transf)

        x,y,z = cmds.pointPosition(self.missle_transf+'.vtx[4]')
        cmds.move(x,y,z,list_wings[0])

        x,y,z = cmds.pointPosition(self.missle_transf+'.vtx[9]')
        cmds.move(x,y,z,list_wings[1])
        cmds.xform(list_wings[1], ro = (0,0,90))

        x,y,z = cmds.pointPosition(self.missle_transf+'.vtx[14]')
        cmds.move(x,y,z,list_wings[2])
        cmds.xform(list_wings[2], ro = (0,0,180))

        x,y,z = cmds.pointPosition(self.missle_transf+'.vtx[19]')
        cmds.move(x,y,z,list_wings[3])
        cmds.xform(list_wings[3], ro = (0,0,-90)) 





vostok = Carrier_rocket(height = 60, radius = 3, rocket_stage = 54, nozzle_count = 6)
vostok.create_stage() 
vostok.create_nozzle()
vostok.create_cabin()

vostok.rocket_launch()



tomohawk = Missle(height = 12, radius =1)
tomohawk.create_boudy()
tomohawk.create_fuse()
tomohawk.create_wings()
tomohawk.create_target()