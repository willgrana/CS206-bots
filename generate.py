#Will Grana

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0
z = 0.5

for i in range(5):
	x=i
	for j in range(5):
		y=j
		l = 1
		w = 1
		h = 1
		for k in range(10):
			z=k+0.5
			pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[l,w,h])
			l = l*0.9
			w = w*0.9
			h = h*0.9
			print("z:" +str(z))
pyrosim.End()
