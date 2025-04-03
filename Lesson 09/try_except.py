import builtins

print("""\nUnderstanding Why We Need try-except
      
- When we write code, some operations may cause errors
  (e.g., dividing by zero, wrong input type, file not found, etc.).
- If an error occurs, the program usually stops running (crashes).
- The try-except block prevents crashes by catching errors and handling them gracefully.

""")

print("\nWriting a Basic try-except Block")
try:
    num = int(input("Enter a number: "))  # User inputs a number
    result = 10 / num  # Divide 10 by the number
    print("Result:", result)  # Print result
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  # If num is 0
except ValueError:
    print("Error: Please enter a valid number.")  # If user enters text instead of a number
except Exception as e:
    print("An unexpected error occurred:", e)  # Catch any other error


print("\nUsing else with finally")
try:
    num = float(input("Enter a number: "))
    result = 100 / num
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)
else:
    print(f"Result is: {result:.2f}")  # Runs only if try block is successful
finally:
    print("Execution completed.")  # Always runs


print("\nBuilt-in Errors")
# Filter out only the exceptions (which are classes)
exceptions = [name for name, obj in vars(builtins).items() if isinstance(obj, type) and issubclass(obj, BaseException)]

# Print the list of exception names
for exception in exceptions:
    print(exception)