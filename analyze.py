#Will Grana

import numpy as np
import matplotlib.pyplot

angles = np.load("data/targetAngles.npy")
#backLegSensorValues = np.load("data/backLegSensorValues.npy")
#frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#print(backLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.plot(angles, label="angles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
