import math

# Method 1: Calculate the square root of a number
num = 16
sqrt_num = math.sqrt(num)
print(f"\nSquare root of {num} is: {sqrt_num}")

# Method 2: Calculate the factorial of a number
factorial_num = 5
factorial_result = math.factorial(factorial_num)
print(f"\nFactorial of {factorial_num} is: {factorial_result}")

# Method 3: Calculate the power of a number (e.g., 2 raised to the power of 3)
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"\n{base} raised to the power of {exponent} is: {power_result}")

# Method 4: Get the value of pi
pi_value = math.pi
print(f"\nValue of pi: {pi_value}")

# Method 5: Find the cosine of an angle (in radians)
angle_in_radians = math.radians(60)  # Convert 60 degrees to radians
cosine_result = math.cos(angle_in_radians)
print(f"\nCosine of 60 degrees is: {cosine_result}")

# Method 6: Round a number to the nearest integer
num_to_round = 3.6
rounded_num = round(num_to_round)
print(f"\nRounded value of {num_to_round} is: {rounded_num}")


print("""\n Explanation of Methods:
math.sqrt(num): Calculates the square root of num. For example, the square root of 16 is 4.

math.factorial(num): Calculates the factorial of a number (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120).

math.pow(base, exponent): Raises base to the power of exponent (e.g., 2^3 = 8).

math.pi: Returns the constant value of π (approximately 3.141592653589793).

math.radians(degrees): Converts an angle from degrees to radians (necessary for trigonometric functions like math.cos).

math.cos(radians): Calculates the cosine of an angle (provided in radians).

round(num): Rounds a floating-point number to the nearest integer.""")