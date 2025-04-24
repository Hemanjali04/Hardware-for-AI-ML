
import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
np.random.seed(42)
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

# Weights and biases
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# Training parameters
lr = 0.1
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward propagation
    hidden_input = np.dot(X, hidden_weights) + hidden_bias
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, output_weights) + output_bias
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)

    error_hidden = d_output.dot(output_weights.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Updating weights and biases
    output_weights += hidden_output.T.dot(d_output) * lr
    output_bias += np.sum(d_output, axis=0, keepdims=True) * lr
    hidden_weights += X.T.dot(d_hidden) * lr
    hidden_bias += np.sum(d_hidden, axis=0, keepdims=True) * lr

# Final predictions
print("XOR predictions after training:")
for i in range(len(X)):
    print(f"{X[i]} => {final_output[i][0]:.4f}")
