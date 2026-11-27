memo = {}

def dpll(clauses, assignment={}):
    key = tuple(sorted(assignment.items()))
    if key in memo:
        return memo[key]
    
    def is_satisfied(clause):
        return any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause)
    
    if all(is_satisfied(clause) for clause in clauses):
        memo[key] = assignment
        return assignment
    
    def is_unsatisfied(clause):
        return all((lit > 0 and not assignment.get(abs(lit), True)) or (lit < 0 and assignment.get(abs(lit), False)) for lit in clause)
    
    if any(is_unsatisfied(clause) for clause in clauses):
        memo[key] = None
        return None
    
    # Process unit clauses
    unit_clauses = [clause for clause in clauses if sum(1 for lit in clause if abs(lit) not in assignment) == 1]
    while unit_clauses:
        unit_clause = unit_clauses.pop()
        unit_lit = next(lit for lit in unit_clause if abs(lit) not in assignment)
        assignment[abs(unit_lit)] = unit_lit > 0
        if dpll(clauses, assignment) is not None:
            return assignment
        else:
            del assignment[abs(unit_lit)]
    
    # Choose a variable that is not yet assigned
    variable = next(lit for clause in clauses for lit in clause if abs(lit) not in assignment)
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

    return results

results = run_tests()
print(" | ".join(results))
