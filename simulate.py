#Will Grana

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
simulation.Save_Values()
#amplitudeBack = np.pi/7
#frequencyBack = 8
#phaseOffsetBack = np.pi/2

#amplitudeFront = np.pi/7
#frequencyFront = 8
#phaseOffsetFront = 0

##physicsClient = p.connect(p.GUI)
##p.setAdditionalSearchPath(pybullet_data.getDataPath())
##
##p.setGravity(0,0,c.GRAVITY)
##planeId = p.loadURDF("plane.urdf")
##robotId = p.loadURDF("body.urdf")
##p.loadSDF("world.sdf")
##pyrosim.Prepare_To_Simulate(robotId)
##backLegSensorValues = np.zeros(c.SIM_STEPS)
##frontLegSensorValues = np.zeros(c.SIM_STEPS)
###print(backLegSensorValues)
##
##targetAnglesBack = np.linspace(0,2*np.pi,c.SIM_STEPS)
##targetAnglesBack = (c.amplitudeBack)*np.sin(c.frequencyBack*targetAnglesBack+c.phaseOffsetBack)
##
##targetAnglesFront = np.linspace(0,2*np.pi,c.SIM_STEPS)
##targetAnglesFront = c.amplitudeFront*np.sin(c.frequencyFront*targetAnglesFront+c.phaseOffsetFront)
##
###np.save("data/targetAngles.npy", targetAngles)
##
##for i in range(c.SIM_STEPS):
##	p.stepSimulation()
##	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
##	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
##	#print(backLegTouch)
##	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_BackLeg",controlMode=p.POSITION_CONTROL,targetPosition=targetAnglesBack[i],maxForce=50)
##	pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_FrontLeg",controlMode=p.POSITION_CONTROL,targetPosition=targetAnglesFront[i],maxForce=50)
##	time.sleep(c.STEP_SIZE_S)
##
##np.save("data/backLegSensorValues.npy", backLegSensorValues)
##np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
###print(backLegSensorValues)
##p.disconnect()
##
