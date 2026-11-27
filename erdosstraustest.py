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

# Print the results along with the values of a, b, c, and d
for i in range(10):
    print(f"Iteration {i + 1}:")
    print(f"  a = {a[i]}")
    print(f"  b = {b[i]}")
    print(f"  c = {c[i]}")
    if d[i] is not None:
        for key, value in d[i].items():
            print(f"  {key} = {value}")
    else:
        print("  No calculations performed.")
    print()
