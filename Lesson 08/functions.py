import math
# Function Demonstrations in Python

print("\n1. Built-in Functions")
print("--------------------")
print("These are pre-defined functions in Python that perform common tasks.\n")

# Example of built-in functions
print("Length of 'Hello':", len("Hello"))
print("Absolute value of -10:", abs(-10))
print("Sum of [1, 2, 3]:", sum([1, 2, 3]))


print("\n2. User-Defined Functions")
print("-------------------------")
print("These are functions created by users to perform specific tasks.\n")

# Example of a user-defined function
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Noor"))


print("\n3. Anonymous (Lambda) Functions")
print("-------------------------------")
print("Lambda functions are small, one-line functions without a name.\n")

# Example of a lambda function
square = lambda x: x * x
print("Square of 5:", square(5))


print("\n4. Recursive Functions")
print("----------------------")
print("A recursive function is a function that calls itself to solve a problem.\n")

# Example of a recursive function
def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


print("\n5. Higher-Order Functions")
print("------------------------")
print("These functions take other functions as arguments or return them.\n")

# Example of a higher-order function
def apply_operation(x, func):
    """Applies a given function to x and returns the result."""
    return func(x)

print("Applying square function to 4:", apply_operation(4, lambda x: x ** 2))


print("\n6. Function Inside a .py File (Module Example)")
print("----------------------------------------------")
print("Functions can be defined in separate files and imported for reuse.\n")

# Example: Suppose we have a file named 'math_operations.py' with the following functions:
# (Uncomment the below lines if you have the file `math_operations.py` in your working directory)
"""
# math_operations.py

def add(a, b):
    \"\"\"Returns the sum of two numbers.\"\"\"
    return a + b

def subtract(a, b):
    \"\"\"Returns the difference between two numbers.\"\"\"
    return a - b
"""

# Importing the module (if it exists)
try:
    import math_operations as mo
    print("Addition (5 + 3):", mo.add(5, 3))
    print("Subtraction (10 - 4):", mo.subtract(10, 4))
except ImportError:
    print("Module 'math_operations' not found. Create it with function definitions.")

print("\n-- End of Function Types Demonstration --")


print("\nBuilt-in functions in python")
functions = [fun for fun in dir(math) if callable(getattr(math, fun)) and not fun.startswith("_")]
print(functions)
