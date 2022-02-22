import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR



class ROBOT:

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for motorName in pyrosim.jointNamesToIndices:
            self.motors[motorName] = MOTOR(motorName)

    def Sense(self,i):
        for key in self.sensors:
            self.sensors[key].Get_Value(i)
        
    def Act(self,i):
        for key in self.motors:
            self.motors[key].Set_Value(self.robotId, i)
            
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

   
