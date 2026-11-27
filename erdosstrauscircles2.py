import matplotlib.pyplot as plt
import numpy as np

# Initialize the arrays
a = [None] * 10
b = [None] * 10
c = [None] * 10
d = [None] * 10

# Set initial values
a[0] = 3
b[0] = 5
c[0] = 18

# Perform calculations and store results in d
for i in range(10):
    if a[i] is not None and b[i] is not None and c[i] is not None:
        d[i] = {
            'a + b': a[i] + b[i],
            'a - b': a[i] - b[i],
            'a + c': a[i] + c[i],
            'a - c': a[i] - c[i],
            'b + c': b[i] + c[i],
            'b - c': b[i] - c[i],
            'a + b + c': a[i] + b[i] + c[i],
            'a - b - c': a[i] - b[i] - c[i]
        }
        # Update the next set of values
        if i < 9:
            a[i + 1] = d[i]['a + b']
            b[i + 1] = d[i]['a + c']
            c[i + 1] = d[i]['b + c']

# Plot settings
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Function to calculate positions ensuring at least 10 pixels apart
def polar_to_cartesian(radius, angle):
    return radius * np.cos(angle), radius * np.sin(angle)

# Plot initial values
initial_angles = np.linspace(0, 2 * np.pi, 3, endpoint=False)
initial_values = [a[0], b[0], c[0]]
for r, angle in zip(initial_values, initial_angles):
    x, y = polar_to_cartesian(r, angle)
    ax.scatter(x, y, c='red', label=f'Initial Value {r}')
    ax.text(x, y, f'{r}', fontsize=12, ha='right')

# Plot calculated values
for i in range(10):
    if d[i] is not None:
        results = list(d[i].values())
        angles = np.linspace(0, 2 * np.pi, len(results), endpoint=False)  # Ensure same length
        for r, angle in zip(results, angles):
            x, y = polar_to_cartesian(r, angle)
            ax.scatter(x, y, label=f'Iteration {i+1} Result {r}')
            ax.text(x, y, f'{r}', fontsize=12, ha='right')

# Configure the plot
ax.set_title("Values in a 360-Degree Pattern")
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))

# Display the plot
plt.show()
