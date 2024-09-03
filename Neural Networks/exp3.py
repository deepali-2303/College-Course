import numpy as np

inputs = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
]

bias = np.zeros(len(inputs[0]))

num_inputs = len(inputs[0])
num_neurons = len(inputs)
weights = np.zeros((num_inputs, num_neurons))

for input_vector in inputs:
    for i in range(num_inputs):
        for j in range(num_neurons):
            weights[i, j] += input_vector[i] * input_vector[j]
        bias[j] += input_vector[j]

test_input = []
for i in range(num_inputs):
    user_input = int(input())
    test_input.append(user_input)

output_A = np.dot(test_input, weights[:, 0]) + bias[0]
output_E = np.dot(test_input, weights[:, 1]) + bias[1]

pattern_labels = {0: 'A', 1: 'E'}

recognized_pattern = np.argmax([output_A, output_E])

print(f"The network recognized pattern: {pattern_labels[recognized_pattern]}")
