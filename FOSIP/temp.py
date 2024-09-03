import matplotlib.pyplot as plt
import numpy as np
import control as ctrl

# Define the open-loop transfer function
numerator = [1, 2]
denominator = [1, 0, 1, -4]

system = ctrl.TransferFunction(numerator, denominator)

# Create a frequency range
omega = np.logspace(-1, 2, 1000)

# Calculate magnitude and phase
magnitude, phase, omega = ctrl.bode(system, omega)

# Plot polar plot
plt.figure()
plt.polar(np.radians(phase), magnitude)
plt.title('Polar Plot of Open-Loop Transfer Function')
plt.show()