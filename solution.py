import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

length = 5
width = 50
height = .5


class SOLUTION:
    def __init__(self, ID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights*2 - 1
        self.myID = ID
        pass

    def Set_ID(self, ID):
        self.myID = ID

    def Mutate(self):
        randrow = random.randint(0,c.numSensorNeurons-1)
        randcol = random.randint(0,c.numMotorNeurons-1)
        self.weights[randrow][randcol] = random.random()*2 - 1
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-7, 0, .5] , size=[length, width, height])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
##        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
##        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])
##        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
##        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
##        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 2], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 2], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute",position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute",position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute",position=[-1,0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
##        pyrosim.Send_Sensor_Neuron(name=0, linkName='Torso')
##        pyrosim.Send_Sensor_Neuron(name=1, linkName='BackLeg')
##        pyrosim.Send_Sensor_Neuron(name=2, linkName='FrontLeg')
##        pyrosim.Send_Motor_Neuron(name=3, jointName='Torso_BackLeg')
##        pyrosim.Send_Motor_Neuron(name=4, jointName='Torso_FrontLeg')
        pyrosim.Send_Sensor_Neuron(name=0, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LowerRightLeg")

        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_LowerRightLeg")

        row = 0

        for i in self.weights:
            column = 0
            for j in i:
                pyrosim.Send_Synapse( sourceNeuronName = row , targetNeuronName = column+3 , weight = j)            
                column = column+1
            row = row+1
            
        pyrosim.End()

    def Start_Simulation(self, G):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py "+G+" "+str(self.myID)+" 2&>1"+" &")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        while os.path.getsize("fitness"+str(self.myID)+".txt")<5:
            time.sleep(0.01)
        infile = open("fitness"+str(self.myID)+".txt", 'r')
        fitness = infile.readline()
        try:
            self.fitness = float(fitness)
        except ValueError as error:
            print(error)
            print("attempted to convert: "+fitness)
            print("ID: "+str(self.myID))
            exit()
        infile.close()
        #print(self.fitness)
        os.system("rm fitness" + str(self.myID) + ".txt")
        G = "DIRECT"
    
    def Evaluate(self, G):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py "+G+" "+str(self.myID)+" &")
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        infile = open("fitness"+str(self.myID)+".txt", 'r')
        self.fitness = float(infile.readline())
        #print(self.fitness)
        infile.close()
        G = "DIRECT"


    
