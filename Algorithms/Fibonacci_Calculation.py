import math


# ----------------------------------------
# Recursive Method (Naive)
# ----------------------------------------
def fib_recursive(n):
    """
    Recursively computes the nth Fibonacci number.
    Time Complexity: Exponential (O(2^n))
    Not efficient for large n due to repeated calculations.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# ----------------------------------------
# Iterative Method (Efficient)
# ----------------------------------------
def fib_iterative(n):
    """
    Iteratively computes the nth Fibonacci number.
    Time Complexity: Linear (O(n))
    Space Complexity: Constant (O(1))
    Best for performance and large n.
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b if n > 0 else a


# ----------------------------------------
# Binet's Formula (Closed Form)
# ----------------------------------------
def fib_binet(n):
    """
    Computes the nth Fibonacci number using Binet's formula.
    Time Complexity: Constant (O(1))
    May lose precision for large n due to floating-point rounding.
    """
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)  # Round to nearest integer


# ----------------------------------------
# Test and Compare All Methods
# ----------------------------------------
def compare_methods(n):
    print(f"Fibonacci number F({n}):")
    print("Recursive:", fib_recursive(n))
    print("Iterative:", fib_iterative(n))
    print("Binet's Formula:", fib_binet(n))


# Example usage
compare_methods(10)
print(f"Fibonacci number F(50) using closed-sum formula: {fib_binet(50)}")
print(f"Fibonacci number F(50) using iterative method: {fib_iterative(50)}")
# print(f"Fibonacci number F(50) using recursive method: {fib_recursive(50)}")   # Note: This will be slow for n=50
