#Will Grana

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("world.sdf")

x = 0
y = 0
z = 0.5

l = 1
w = 1
h = 1

pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])

pyrosim.End()
