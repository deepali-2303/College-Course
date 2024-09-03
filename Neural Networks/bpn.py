import numpy as np

data = np.genfromtxt('data.csv', delimiter=',')
X = data[:, :-1] 
y = data[:, -1]  

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

w_input_hidden = 2 * np.random.random((X.shape[1], 4)) - 1
w_hidden_output = 2 * np.random.random((4, 1)) - 1

learning_rate = 0.3

for epoch in range(10000):
    if epoch < 5: 
        print(f'Weights after iteration {epoch+1}:')
        print('Input to Hidden Weights:')
        print(w_input_hidden)
        print('Hidden to Output Weights:')
        print(w_hidden_output)
    
    hidden_layer_input = np.dot(X, w_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, w_hidden_output)
    predicted_output = sigmoid(output_layer_input)
    
    error = y.reshape(-1, 1) - predicted_output
    
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    error_hidden_layer = d_predicted_output.dot(w_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
        
    w_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    w_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

predicted_output[predicted_output >= 0.5] = 1
predicted_output[predicted_output < 0.5] = -1

accuracy = np.mean(predicted_output == y.reshape(-1, 1)) * 100
print(f'Accuracy: {accuracy:.2f}%')

user_input = np.zeros(3)

user_input[0] = float(input(f'Fever: '))
user_input[1] = float(input(f'Headache: '))
user_input[2] = float(input(f'Jaundice: '))

hidden_layer_input = np.dot(user_input, w_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_input = np.dot(hidden_layer_output, w_hidden_output)
predicted_output = sigmoid(output_layer_input)

predicted_output[predicted_output >= 0.5] = 1
predicted_output[predicted_output < 0.5] = -1

if predicted_output == 1:
    print("Prediction: Dengue")
else:
    print("Prediction: Malaria")
