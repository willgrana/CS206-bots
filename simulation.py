
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self):
        
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,c.GRAVITY)

    def Run(self):
        for i in range(c.SIM_STEPS):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            #print(backLegTouch)
            
            time.sleep(c.STEP_SIZE_S)

    def Save_Values(self):
        for key in self.robot.sensors:
            np.save("data/SensorValues" + str(key)+ ".npy", self.robot.sensors[key])

    def __del__(self):

        p.disconnect()
