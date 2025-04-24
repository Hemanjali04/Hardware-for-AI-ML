
# Challenge 8 – XOR with Multi-layer Perceptron (2-2-1)

import numpy as np

# XOR dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights and biases
np.random.seed(42)
W1 = np.random.uniform(size=(2, 2))  # input → hidden
b1 = np.random.uniform(size=(1, 2))  # hidden bias
W2 = np.random.uniform(size=(2, 1))  # hidden → output
b2 = np.random.uniform(size=(1, 1))  # output bias

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training loop
for epoch in range(epochs):
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(W2.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_output)

    W2 += hidden_output.T.dot(d_predicted_output) * learning_rate
    b2 += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden_output) * learning_rate
    b1 += np.sum(d_hidden_output, axis=0, keepdims=True) * learning_rate

    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Final output
print("Predicted Output after Training:")
print(np.round(predicted_output, 3))
