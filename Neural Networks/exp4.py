
import numpy as np

def step_function(x):
    return 1 if x > 0 else -1

def train_perceptron(X, y, learning_rate, epochs):
    num_features = X.shape[1]
    weights = np.random.rand(num_features)
    bias = np.random.rand()

    for epoch in range(epochs):
        for i in range(len(X)):
            net_input = np.dot(X[i], weights) + bias
            y_pred = step_function(net_input)

            if y_pred != y[i]:
                weights += learning_rate * (y[i] - y_pred) * X[i]
                bias += learning_rate * (y[i] - y_pred)

    return weights, bias

def predict(X, weights, bias):
    net_input = np.dot(X, weights) + bias
    y_pred = np.array([step_function(x) for x in net_input])
    return y_pred


data = np.loadtxt('data.txt', delimiter=';')
print(data)
X = data[:, :-1]
y = data[:, -1]

split_ratio = 0.8
split_index = int(len(X) * split_ratio)
X_train, y_train = X[:split_index], y[:split_index]
X_test, y_test = X[split_index:], y[split_index:]

learning_rate = 0.1
epochs = 1000
weights, bias = train_perceptron(X_train, y_train, learning_rate, epochs)


user_input = []
for feature in ['smoothness', 'softness', 'shine', 'wrinkle proneness', 'friction', 'fluidity']:
    value = float(input(f'Enter {feature}: '))
    user_input.append(value)


user_input.append(1)


user_input = np.array(user_input)


user_input = user_input[:len(weights)]


predicted_label = step_function(np.dot(user_input, weights) + bias)

if predicted_label == 1:
    print("The input is classified as silk.")
else:
    print("The input is classified as non-silk.")
