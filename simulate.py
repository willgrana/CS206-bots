#Will Grana

import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for i in range(1000):
	p.stepSimulation()
	time.sleep(1/40)
	print(i)
p.disconnect()

