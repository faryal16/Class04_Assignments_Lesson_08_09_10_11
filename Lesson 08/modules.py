"""
What is a Module in Python?
----------------------------
A module in Python is a file that contains Python code (functions, classes, variables, or runnable code) and is used to organize and reuse code efficiently.

Types of Modules in Python:
1. Built-in Modules
2. User-Defined Modules
3. External Modules
"""

# 1. Built-in Modules (Standard Library)
import math
import random
import os
import sys

# Example usage of built-in modules
print("\nSquare root of 25:", math.sqrt(25)) 
print("\nRandom number between 1 and 10:", random.randint(1, 10))
print("\nCurrent working directory:", os.getcwd())
print("\nPython version:", sys.version)

# 2. User-Defined Module Example (mymodule.py)
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Testing the custom module functions
if __name__ == "__main__":
    print("\nAddition:", add(5, 3))  # Output: 8
    print("\nSubtraction:", subtract(10, 4))  # Output: 6
    print("\nMultiplication:", multiply(6, 7))  # Output: 42
    print("\nDivision:", divide(8, 2))  # Output: 4.0

# 3. External Modules (Third-party Libraries)
# Example of using an external module (requests)
# Install using: pip install requests
try:
    import requests
    response = requests.get("https://www.google.com", timeout=10)
    print("\nResponse Status Code:", response.status_code)
except ImportError:
    print("\nError: Requests module not installed. Install it using: pip install requests")
except requests.exceptions.RequestException as e:
    print(f"\nRequest Error: {e}")

# Import Methods

# Basic Import
import math
print(math.pi)  # Output: 3.141592653589793
print(f"{math.pi:.2f}")  # Output: 3.14


# Import with Alias
try:
    import numpy as np
    print(np.array([1, 2, 3]))
except ImportError:
    print("\nError: NumPy is not installed. Install it using 'pip install numpy'.")

# Import Specific Functions
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793

# Import Everything (Not Recommended)
from math import *
print(sin(0))  # Output: 0.0

# Filter out modules containing "_"
filtered_modules = [mod for mod in sys.builtin_module_names if "_" not in mod]

print("\nBuilt-in Modules in python")
print(filtered_modules)