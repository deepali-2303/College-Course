import numpy as np

def symmetric_hard_limit(x):
    return np.where(x >= 0, 1, -1)

input_data = np.array([-2, -1, 0, 1, 2, 3, 4])
output_symmetric_hard_limit = symmetric_hard_limit(input_data)
print("Symmetric Hard Limit:", output_symmetric_hard_limit)