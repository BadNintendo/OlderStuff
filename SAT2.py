memo = {}

def dpll(clauses, assignment={}):
    key = tuple(sorted(assignment.items()))
    if key in memo:
        return memo[key]

    def is_satisfied(clause):
        return any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause)

    def is_unsatisfied(clause):
        return all((lit > 0 and not assignment.get(abs(lit), True)) or (lit < 0 and assignment.get(abs(lit), False)) for lit in clause)

    if all(is_satisfied(clause) for clause in clauses):
        memo[key] = assignment
        return assignment

    if any(is_unsatisfied(clause) for clause in clauses):
        memo[key] = None
        return None

    # Pure literal elimination
    pure_literals = set()
    all_literals = {lit for clause in clauses for lit in clause}
    for lit in all_literals:
        if -lit not in all_literals:
            pure_literals.add(lit)
    
    for lit in pure_literals:
        assignment[abs(lit)] = lit > 0

    # Process unit clauses
    unit_clauses = [clause for clause in clauses if sum(1 for lit in clause if abs(lit) not in assignment) == 1]
    while unit_clauses:
        unit_clause = unit_clauses.pop()
        unit_lit = next(lit for lit in unit_clause if abs(lit) not in assignment)
        assignment[abs(unit_lit)] = unit_lit > 0
        result = dpll(clauses, assignment)
        if result is not None:
            memo[key] = result
            return result
        del assignment[abs(unit_lit)]

    # Choose the first unassigned variable
    unassigned_vars = {abs(lit) for clause in clauses for lit in clause if abs(lit) not in assignment}
    if not unassigned_vars:
        memo[key] = None
        return None

    variable = unassigned_vars.pop()
    for value in [True, False]:
        result = dpll(clauses, {**assignment, variable: value})
        if result is not None:
            memo[key] = result
            return result
    memo[key] = None
    return None

def run_tests():
    test_cases = [
        ([[1, -2], [2, 3], [-1, -3]], True),
        ([[1], [-1]], False),
        ([[1, 2], [-1, -2]], False),
        ([[1, 2], [1, -2], [-1, 2], [-1, -2]], True),
        ([[1, 2, 3], [-1, -2], [2, -3], [-2, 3]], True)
    ]

    results = []
    for i, (clauses, expected) in enumerate(test_cases):
        memo.clear()  # Clear memoization before each test
        result = dpll(clauses) is not None
        results.append(f"Test {i + 1}: {'Pass' if result == expected else 'Fail'}")

    return results

results = run_tests()
print(" | ".join(results))
