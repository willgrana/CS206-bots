#Will Grana

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
#print(backLegSensorValues)

for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#print(backLegTouch)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_BackLeg",controlMode=p.POSITION_CONTROL,targetPosition=random.uniform(np.pi/-2.0,np.pi/2.0),maxForce=100)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_FrontLeg",controlMode=p.POSITION_CONTROL,targetPosition=random.uniform(np.pi/-2.0,np.pi/2.0),maxForce=100)
	time.sleep(1/40)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
#print(backLegSensorValues)
p.disconnect()

