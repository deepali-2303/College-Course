import numpy as np
import matplotlib.pyplot as plt

def binary_step_activation(x):
    return np.where(x >= 0, 1, 0)

arr = np.array([-3, -2, -1, 0, 1, 2, 3])
output = binary_step_activation(arr)
print("Binary Step activation function output:", output)

plt.plot(arr, output)
plt.xlabel("input")
plt.ylabel("output")

# Set the limits and ticks to center the plot
plt.xlim(-3, 3)
plt.ylim(-0.5, 1.5)
plt.xticks(np.arange(-3, 4))
plt.yticks([0, 1])

# Set the origin to (0, 0)
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.title("Binary Step")

plt.show()
