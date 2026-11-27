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
                # Check if resolve or limit are present in the values and results
                values = {a, b, c}
                if resolve in values or limit in values:
                    # Check if limit is part of at least two values or results
                    occurrences = sum(x in {resolve, limit} for x in values) + \
                                  sum(result in {resolve, limit} for result in results.values())
                    if occurrences >= 2:
                        # Check if 100 is in the evaluations from a, b, or c in any order
                        if any(resolve in {a, b, c} for _ in range(2)):
                            # Ensure limit is part of calculations and check for relevant results
                            for operation, result in results.items():
                                if result != resolve and result != limit:
                                    # Store solutions where the result is unique and relevant
                                    solutions.append((a, b, c, operation, result))
    
    return solutions

resolve = 100  # Example value for resolve
limit = 245  # Example limit value

solutions = basic_math_operations(resolve, limit)

if solutions:
    for solution in solutions:
        a, b, c, operation, result = solution
        print(f"a = {a}, b = {b}, c = {c}")
        print(f"Operation: {operation}, Result: {result}")
else:
    print(f"No solutions found for resolve = {resolve} within the limit {limit}")
