import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x + 3)**2

def gradient(x):
    return 2 * (x + 3)

x_start = 2
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 1000

x = x_start
for i in range(max_iterations):
    grad = gradient(x)
    x_new = x - learning_rate * grad

    if abs(x_new - x) < tolerance:
        break
    x = x_new

print(f"Local minima found at x = {x:.6f}")
print(f"Function value at local minima: y = {function(x):.6f}")

x_vals = np.linspace(-6, 3, 100)
y_vals = function(x_vals)

plt.plot(x_vals, y_vals, label='y = (x + 3)²', color='blue')
plt.scatter(x, function(x), color='red', label='Local Minima', zorder=5)
plt.show()
