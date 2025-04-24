import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# OR gate dataset
data = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

# Separate input and output
X = data[:, :2]
y = data[:, 2]

# Add bias to inputs
X_bias = np.hstack([np.ones((X.shape[0], 1)), X])

# Initialize weights
weights = np.random.randn(3)
lr = 0.1

# Store decision boundaries
boundaries = []

# Perceptron training
for epoch in range(10):
    for i in range(len(X_bias)):
        xi = X_bias[i]
        target = y[i]
        prediction = 1 if np.dot(weights, xi) >= 0 else 0
        error = target - prediction
        weights += lr * error * xi
        if weights[2] != 0:
            slope = -weights[1] / weights[2]
            intercept = -weights[0] / weights[2]
            boundaries.append((slope, intercept))

# Plot setup
fig, ax = plt.subplots(figsize=(8, 6))

for i, label in enumerate(y):
    color = 'red' if label == 0 else 'blue'
    ax.scatter(X[i, 0], X[i, 1], color=color, label=str(label) if i in [0, 1] else "")

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_title("Perceptron Learning Animation")
ax.grid(True)

line, = ax.plot([], [], 'k-', lw=2)

# Update function
def update(frame):
    slope, intercept = boundaries[frame]
    x_vals = np.linspace(-0.5, 1.5, 100)
    y_vals = slope * x_vals + intercept
    line.set_data(x_vals, y_vals)
    ax.legend([line], [f"Step {frame + 1}"])
    return line,

# Animate and display inline
ani = animation.FuncAnimation(fig, update, frames=len(boundaries), interval=700, blit=True)
HTML(ani.to_jshtml())

# Optional: Save as GIF
ani.save("perceptron_learning_animation.gif", writer='pillow')