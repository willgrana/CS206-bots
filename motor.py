import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:

    def Prepare_To_Act(self):
        targetAngles = np.linspace(0,2*np.pi,c.SIM_STEPS)
        targetAngles = (self.amplitude)*np.sin(self.frequency*targetAngles+self.phaseOffset)
        return targetAngles

    def Set_Value(self, robotId, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName=self.motorName,controlMode=p.POSITION_CONTROL,targetPosition=self.targetAngles[i],maxForce=50)


    def __init__(self, motorName):
        self.motorName = motorName
        self.amplitude = c.amplitudeBack
        self.frequency = c.frequencyBack
        self.phaseOffset = c.phaseOffsetBack
        self.targetAngles = self.Prepare_To_Act()
        
