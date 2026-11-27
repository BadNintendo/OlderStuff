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

# Set up the plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Plot initial values
initial_angles = np.linspace(0, 2 * np.pi, 3, endpoint=False)
initial_values = [a[0], b[0], c[0]]
ax.scatter(initial_angles, initial_values, c='red', label='Initial Values')

# Plot calculated values
for i in range(10):
    if d[i] is not None:
        results = list(d[i].values())
        angles = np.linspace(0, 2 * np.pi, len(results), endpoint=False)  # Ensure same length
        ax.scatter(angles, results, label=f'Iteration {i+1}')

# Configure the plot
ax.set_title("Values in a 360-Degree Pattern")
ax.set_rmax(100)  # Set maximum radius for better visibility
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))

# Display the plot
plt.show()
