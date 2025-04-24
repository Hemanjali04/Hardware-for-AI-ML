
import numpy as np

# Sigmoid function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Perceptron class with sigmoid activation
class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def predict(self, inputs):
        total = np.dot(inputs, self.weights) + self.bias
        return sigmoid(total)

    def train(self, inputs, targets, learning_rate=0.1, epochs=10000):
        for _ in range(epochs):
            for i in range(len(inputs)):
                output = self.predict(inputs[i])
                error = targets[i] - output
                delta = error * sigmoid_derivative(output)
                self.weights += learning_rate * delta * inputs[i]
                self.bias += learning_rate * delta

# NAND gate training
if __name__ == "__main__":
    X_nand = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y_nand = np.array([1, 1, 1, 0])

    model = Perceptron(2)
    model.train(X_nand, Y_nand)

    print("NAND predictions after training:")
    for x in X_nand:
        print(f"{x} => {model.predict(x):.4f}")
