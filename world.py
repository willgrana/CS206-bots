import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
class WORLD:

    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
