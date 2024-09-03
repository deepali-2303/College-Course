import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def neuron(inputs, weights):
    # Calculate the weighted sum
    weighted_sum = np.dot(inputs, weights)
    
    # Apply the sigmoid activation function
    output = sigmoid(weighted_sum)
    
    return output

def or_gate(x1, x2):
    # Define weights and bias for the OR gate
    weights = np.array([1, 1])
    bias = -0.2  # Adjust bias as needed (tuned to -0.5)
    
    # Create input array
    inputs = np.array([x1, x2])
    
    # Calculate the output of the OR gate
    output = neuron(inputs, weights) + bias
    # print(output)
    if output >= 0.5:  # Threshold is 0.5
        return 1
    else:
        return 0





def and_gate(x1, x2):
    # Define weights and bias for the AND gate
    weights = np.array([1, 1])
    bias = -0.3  # Adjust bias as needed (tuned to -1.5)
    
    # Create input array
    inputs = np.array([x1, x2])
    
    # Calculate the output of the AND gate
    output = neuron(inputs, weights) + bias
    # print(output)
    if output >= 0.5:  # Threshold is 0.5
        return 1
    else:
        return 0

def not_gate(x1):
    # Define weights and bias for the NOT gate
    weights = np.array([-1])
    bias = 0  # No bias needed for NOT gate
    
    # Create input array
    inputs = np.array([x1])
    
    # Calculate the output of the NOT gate
    output = neuron(inputs, weights) + bias
    # print(output)
    if output >= 0.5:  # Threshold is 0.5
        return 1
    else:
        return 0

# Test the gates
print("OR Gate:")
print("OR(0, 0) =", or_gate(0, 0))
print("OR(0, 1) =", or_gate(0, 1))
print("OR(1, 0) =", or_gate(1, 0))
print("OR(1, 1) =", or_gate(1, 1))

print("\nAND Gate:")
print("AND(0, 0) =", and_gate(0, 0))
print("AND(0, 1) =", and_gate(0, 1))
print("AND(1, 0) =", and_gate(1, 0))
print("AND(1, 1) =", and_gate(1, 1))

print("\nNOT Gate:")
print("NOT(0) =", not_gate(0))
print("NOT(1) =", not_gate(1))

def half_adder(a, b):
    # Calculate the sum (S) using an XOR gate
    sum_out = xor_gate(a, b)
    
    # Calculate the carry (C) using an AND gate
    carry_out = and_gate(a, b)
    
    return sum_out, carry_out

# Define XOR gate using the OR, AND, and NOT gates
def xor_gate(x1, x2):
    # Use OR, AND, and NOT gates to implement XOR
    or_result = or_gate(x1, x2)
    and_result1 = and_gate(x1, not_gate(x2))
    and_result2 = and_gate(not_gate(x1), x2)
    
    # Use OR gate to combine the AND results
    xor_result = or_gate(and_result1, and_result2)
    
    return xor_result

# Test the half-adder
print("\nHalf-Adder:")
print("half_adder(0, 0) =", half_adder(0, 0))
print("half_adder(0, 1) =", half_adder(0, 1))
print("half_adder(1, 0) =", half_adder(1, 0))
print("half_adder(1, 1) =", half_adder(1, 1))


