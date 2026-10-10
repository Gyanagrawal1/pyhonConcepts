def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("--- Recursion ---")
print("Factorial of 5 is:", factorial(5))
