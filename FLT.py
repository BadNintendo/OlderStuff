def basic_math_operations(resolve, limit):
    solutions = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                results = {
                    "a + b": a + b,
                    "a - b": a - b,
                    "a + c": a + c,
                    "a - c": a - c,
                    "b + c": b + c,
                    "b - c": b - c,
                    "a + b + c": a + b + c,
                    "a - b - c": a - b - c
                }
                # Check if resolve and limit are present in at least two of a, b, c
                values = {a, b, c}
                if len(values & {resolve, limit}) >= 2:
                    # Check if any result matches the value of resolve or limit
                    if any(result == resolve or result == limit for result in results.values()):
                        solutions.append((a, b, c, results))
    
    return solutions

resolve = 100  # Example value for resolve
limit = 148  # Example limit value

solutions = basic_math_operations(resolve, limit)

if solutions:
    for solution in solutions:
        a, b, c, results = solution
        print(f"a = {a}, b = {b}, c = {c}")
        for operation, result in results.items():
            if result == resolve or result == limit:
                print(f"Operation: {operation}, Result: {result}")
else:
    print(f"No solutions found for resolve = {resolve} within the limit {limit}")
