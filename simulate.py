#Will Grana

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

amplitudeBack = np.pi/7
frequencyBack = 8
phaseOffsetBack = np.pi/2

amplitudeFront = np.pi/7
frequencyFront = 8
phaseOffsetFront = 0

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

targetAnglesBack = np.linspace(0,2*np.pi,1000)
targetAnglesBack = (amplitudeBack)*np.sin(frequencyBack*targetAnglesBack+phaseOffsetBack)

targetAnglesFront = np.linspace(0,2*np.pi,1000)
targetAnglesFront = amplitudeFront*np.sin(frequencyFront*targetAnglesFront+phaseOffsetFront)

#np.save("data/targetAngles.npy", targetAngles)

for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	#print(backLegTouch)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_BackLeg",controlMode=p.POSITION_CONTROL,targetPosition=targetAnglesBack[i],maxForce=50)
	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_FrontLeg",controlMode=p.POSITION_CONTROL,targetPosition=targetAnglesFront[i],maxForce=50)
	time.sleep(1/120)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
#print(backLegSensorValues)
p.disconnect()

