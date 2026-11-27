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
    
    unit_clause = next((clause for clause in clauses if sum(1 for lit in clause if abs(lit) not in assignment) == 1), None)
    if unit_clause:
        unit_lit = next(lit for lit in unit_clause if abs(lit) not in assignment)
        return dpll(clauses, {**assignment, abs(unit_lit): unit_lit > 0})
    
    variable = next(lit for clause in clauses for lit in clause if abs(lit) not in assignment)
    result = dpll(clauses, {**assignment, abs(variable): True}) or dpll(clauses, {**assignment, abs(variable): False})
    memo[key] = result
    return result

clauses = [[1, -2], [2, 3], [-1, -3]]

result = dpll(clauses)
print(f"SAT: {result}")