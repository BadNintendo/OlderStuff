import math

def common_prime_factor(a, b, c):
    # Function to check if a, b, c have a common prime factor
    def prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    
    return prime_factors(a) & prime_factors(b) & prime_factors(c)

def is_valid_beal(A, x, B, y, C, z):
    # Check if A^x + B^y = C^z and they have a common prime factor
    if A**x + B**y == C**z and common_prime_factor(A, B, C):
        return True
    return False

def main():
    highest_value = 99999999
    current_value = highest_value
    
    while current_value > 0:
        A, B, C, x, y, z = current_value, current_value - 1, current_value - 2, 3, 3, 3  # Example values, change as needed
        
        if is_valid_beal(A, x, B, y, C, z):
            print(f"Valid Beal: A={A}, B={B}, C={C}, x={x}, y={y}, z={z}")
        else:
            pass  # Ignore invalid numbers
        
        current_value -= 1
        continue

if __name__ == "__main__":
    main()
