import numpy as np
from math import exp

#asking for user inputs
print("Enter number of neurons: ")
n = int(input())
x = np.array([])
print("Enter input values for each neuron: ")
for i in range(n):
  value = int(input())
  x = np.append(x,value)

w = np.array([])
print("Enter weights for each neuron : ")
for i in range(n):
  value = int(input())
  w = np.append(w,value)

print("Enter bias value: ")
b = int(input())


threshold = int(input("Enter threshold value: "))

#to caculate net output
def calculate_net_output(w,x,b):
  mul = 0
  for i in range(n):
    mul = mul + w[i]*x[i]
  return mul + b


# symmetric hard limit transfer function
def symmetric_hard_limit(net_output):
  if net_output>=0:
    return 1
  else:
    return -1

#Binary step activation function
def binary_step_activation(net_output):
  if net_output>=threshold:
    return 1
  else:
    return 0
  
#bipolar step activation function
def bipolar_step_activation(net_output): 
  if net_output>=threshold:
    return 1
  else:
    return -1
  

#saturating linear transfer function
def saturating_linear_transfer(net_output):
  if net_output<=0:
    return 0
  elif  net_output>1:
    return 1
  else:
    return net_output
  

#A hyperbolic tangent sigmoid (tansig) transfer function
def hyperbolic_tangent_sigmoid(net_output):
  x = net_output
  return (exp(x)-exp(-x))/(exp(x)-exp(-x))


#log sigmoid function
def log_sigmoid_function(net_output):
  x=net_output
  return 1/(1+exp(-x))

net_output = calculate_net_output(w,x,b)

print("Net Output: ",net_output)

print("Output of symmetric hard limit function: ",symmetric_hard_limit(net_output))
print("Output of Binary step activation function: ",binary_step_activation(net_output))
print("Output of Bipolar step activation function: ",bipolar_step_activation(net_output))
print("Output of saturating linear transfer function: ",saturating_linear_transfer(net_output))
print("Output of hyperbolic tangent sigmoid function: ",hyperbolic_tangent_sigmoid(net_output))
print("Output of log sigmoid function: ",log_sigmoid_function(net_output))