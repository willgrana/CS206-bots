import solution
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        #self.parent = solution.SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1

    def Print(self):
        for key in self.parents:
            print("\nParent Fitness: "+str(self.parents[key].fitness)+" Child Fitness: "+str(self.children[key].fitness)+"\n")

    def Show_Best(self):
        self.Select()
        best_fit = 10000.00
        for key in self.parents:
            if self.parents[key].fitness<best_fit:
                best = copy.deepcopy(self.parents[key])
                best_fit = self.parents[key].fitness
        best.Evaluate("GUI")
        pass
    
    def Spawn(self):
        #self.child = copy.deepcopy(self.parent)
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1
        pass

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()
        pass

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness<self.parents[key].fitness:
                self.parents[key] = self.children[key]
        pass

    def Evaluate(self, G, solutions):
        for key in solutions:
            solutions[key].Start_Simulation(G)
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
        

    def Evolve_For_One_Generation(self, G):
        self.Spawn()
        self.Mutate()

        self.Evaluate(G, self.children)
        self.Print()
        self.Select()
        pass
    
    def Evolve(self):
        G = "DIRECT"
        
##        G = "GUI"
##        self.parent.Evaluate(G)
##        G = "DIRECT"
        self.Evaluate(G, self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            print(currentGeneration)
            self.Evolve_For_One_Generation(G)
    
