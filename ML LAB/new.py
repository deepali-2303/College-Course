import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data for polynomial regression
X = np.linspace(0, 10, 20)
Y = 0.5*X**2 - 2*X + 3 + np.random.normal(0, 2, 20)  # Polynomial equation with noise

# Create DataFrame
df = pd.DataFrame({'X': X, 'Y': Y})

# Save DataFrame to CSV
df.to_csv('example.csv', index=False)

print("CSV dataset for polynomial regression generated successfully.")
