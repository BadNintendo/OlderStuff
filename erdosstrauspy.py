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
        # Increase b and c values for the next iteration
        if i < 9:
            a[i + 1] = a[i] + 1
            b[i + 1] = b[i] + 1
            c[i + 1] = c[i] + 1

# Print the results
for i in range(10):
    print(f"Iteration {i + 1}:")
    if d[i] is not None:
        for key, value in d[i].items():
            print(f"  {key} = {value}")
    else:
        print("  No calculations performed.")
    print()