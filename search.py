import os
import hillclimber
import parallelhillclimber

#for i in range(5):
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")



phc = parallelhillclimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
