#Will Grana

import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	x=0
	y=-6
	z=0.5
	l=1
	w=1
	h=1
	pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso",pos=[0,0,1.5],size=[1,1,1])
	pyrosim.Send_Joint(name="Torso_FrontLeg",parent="Torso",child="FrontLeg",type="revolute",position=[0.5,0,1])
	pyrosim.Send_Cube(name="FrontLeg",pos=[0.5,0,-0.5],size=[1,1,1])
	pyrosim.Send_Joint(name="Torso_BackLeg",parent="Torso",child="BackLeg",type="revolute",position=[-0.5,0,1])
	pyrosim.Send_Cube(name="BackLeg",pos=[-0.5,0,-0.5],size=[1,1,1])
	pyrosim.End()

Create_World()
Create_Robot()
