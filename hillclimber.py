import solution
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()
        pass

    def Print(self):
        print("\nParent Fitness: "+str(self.parent.fitness)+" Child Fitness: "+str(self.child.fitness))

    def Show_Best(self):
        self.Select()
        self.parent.Evaluate("GUI")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        pass

    def Mutate(self):
        self.child.Mutate()
        pass

    def Select(self):
        
        if self.child.fitness<self.parent.fitness:
            self.parent = self.child
        pass

    def Evolve_For_One_Generation(self, G):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate(G)
        self.Print()
        self.Select()
    
    def Evolve(self):
        G = "GUI"
        self.parent.Evaluate(G)
        G = "DIRECT"
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(G)
        pass
    
