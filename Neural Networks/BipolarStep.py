import numpy as np
import matplotlib.pyplot as plt

def bipolar_step(x):
    return np.where(x>=1,1,-1)

input = np.array([-1,-2,-3,0,1,2])
output = bipolar_step(input)

print("Bipolar Step Activation Function output : ",output)

plt.plot(input,output)
plt.xlabel("input")
plt.ylabel("output")
plt.ylim(-5,5)
plt.xlim(-5,5)
plt.title("Bipolar Step")
plt.show()