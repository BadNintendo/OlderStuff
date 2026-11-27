memo = {}

def is_satisfied(clause, assignment):
    return any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause)

def is_unsatisfied(clause, assignment):
    return all((lit > 0 and not assignment.get(abs(lit), True)) or (lit < 0 and assignment.get(abs(lit), False)) for lit in clause)

def dpll(clauses, assignment={}):
    key = tuple(sorted(assignment.items()))
    if key in memo:
        return memo[key]

    if all(is_satisfied(clause, assignment) for clause in clauses):
        memo[key] = assignment
        return assignment

    if any(is_unsatisfied(clause, assignment) for clause in clauses):
        memo[key] = None
        return None

    # Pure literal elimination
    all_literals = {lit for clause in clauses for lit in clause}
    pure_literals = {lit for lit in all_literals if -lit not in all_literals}
    for lit in pure_literals:
        assignment[abs(lit)] = lit > 0

    # Process unit clauses
    def process_unit_clauses():
        unit_clauses = [clause for clause in clauses if sum(1 for lit in clause if abs(lit) not in assignment) == 1]
        while unit_clauses:
            unit_clause = unit_clauses.pop()
            unit_lit = next((lit for lit in unit_clause if abs(lit) not in assignment), None)
            if unit_lit is None:
                continue
            assignment[abs(unit_lit)] = unit_lit > 0
            clauses[:] = [clause for clause in clauses if not is_satisfied(clause, assignment)]
            unit_clauses = [clause for clause in clauses if sum(1 for lit in clause if abs(lit) not in assignment) == 1]
        return None

    process_unit_clauses()

    if all(is_satisfied(clause, assignment) for clause in clauses):
        memo[key] = assignment
        return assignment

    if any(is_unsatisfied(clause, assignment) for clause in clauses):
        memo[key] = None
        return None

    unassigned_vars = {abs(lit) for clause in clauses for lit in clause if abs(lit) not in assignment}
    if not unassigned_vars:
        memo[key] = None
        return None

    variable = unassigned_vars.pop()
    result_true = dpll(clauses, {**assignment, abs(variable): True})
    if result_true is not None:
        memo[key] = result_true
        return result_true

    result_false = dpll(clauses, {**assignment, abs(variable): False})
    memo[key] = result_false
    return result_false

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

    return " | ".join(results)

results = run_tests()
print(results)
