import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy as np

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solutionID):
        self.timeOnGround = 0
        self.z = np.zeros(1500)
        self.legsTogether = 0
        #self.torsoOnGround = 0
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        self.outfile = open("tmp"+str(solutionID)+".txt", 'w')
        os.system("rm brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timeStep):
        self.timeStep = timeStep
        legs = np.array([0,0,0,0])
        j = 0
        z = 0
        #print(self.sensors)
        for i in self.sensors:
            self.sensor = self.sensors[i]
            #self.sensor.Get_Value(self.timeStep)
            val = self.sensor.Get_Value(self.timeStep)
            self.timeOnGround += val+1
            if z==2 or z==4 or z==6 or z==8:
                legs[j] = val
                j+=1
            #print(self.sensor.Get_Value(self.timeStep))
            z+=1
        #print(np.sum(legs))
        if np.sum(legs) == 4:
            self.legsTogether+=1
        if np.sum(legs) == -4:
            self.legsTogether+=1
        stateOfLinkZero = p.getLinkState(self.robotId,0)[0]
        zCoordinateOfLinkZero = stateOfLinkZero[2]
        self.z[timeStep] = zCoordinateOfLinkZero
        

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                desiredAngle = desiredAngle*c.motorJointRange
                self.motors[jointName].Set_Values(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        #stateOfLinkZero = p.getLinkState(self.robotId,0)[0]
        #xCoordinateOfLinkZero = stateOfLinkZero[0]
        #print(type(xCoordinateOfLinkZero))
        #print(xCoordinateOfLinkZero)
        #fitness = self.timeOnGround - (3000*np.amax(self.z))
        #fitness = -10*np.amax(self.z) - (self.timeOnGround/500)
        #print(self.legsTogether) (-1000*np.amax(self.z)) 
        fitness = -1.5*self.legsTogether - 200*np.amax(self.z)
        self.outfile.write(str(fitness))
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        self.outfile.close()
        #exit()
        
