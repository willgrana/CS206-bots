import pybullet as p
import pybullet_data
import time
import world
import robot


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.robot = robot.ROBOT()
        self.world = world.WORLD()


    def run(self):
        for i in range(1500):
            #print(i)
            time.sleep(1 / 240)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()


    def __del__(self):
        p.disconnect()

