# Python Concepts: Control Modules & Functions, Exception Handling, File Handling, Math & Date Time Calendar

## 📌 Overview
This repository contains Python examples and explanations for key concepts, including:
- **Control Modules & Functions**: Organizing and reusing code with functions and modules.
- **Exception Handling**: Managing errors effectively using `try-except` blocks.
- **File Handling**: Reading from and writing to files.
- **Math & Date Time Calendar**: Using Python’s built-in libraries for mathematical operations and date-time manipulation.

---

## 📜 Lesson 08: Control Modules & Functions
### 📌 Topics Covered:
- Creating and using functions (`def` keyword, arguments, return values).
- Importing and using modules (`import`, `from ... import ...`).
- Creating custom modules and importing them.
- Using built-in Python modules.

### 🔹 Example:
```python
# Function Example
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

```python
# Importing a custom module
import my_module
my_module.hello_world()
```

---

## 📜 Lesson 09: Exception Handling
### 📌 Topics Covered:
- Handling errors using `try-except` blocks.
- Using `finally` and `else` with exception handling.
- Raising custom exceptions using `raise`.

### 🔹 Example:
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
finally:
    print("Execution completed.")
```

---

## 📜 Lesson 10: File Handling
### 📌 Topics Covered:
- Opening and closing files (`open()`, `close()`).
- Reading and writing files (`read()`, `write()`).
- Working with different file modes (`r`, `w`, `a`).
- Using `with` statement for better file management.

### 🔹 Example:
```python
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 📜 Lesson 11: Math & Date Time Calendar
### 📌 Topics Covered:
- Performing mathematical operations using the `math` module.
- Working with dates and times using the `datetime` module.
- Using the `calendar` module to display calendars.

### 🔹 Example:
```python
import math
print("Square root of 16:", math.sqrt(16))
```

```python
import datetime
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)
```

```python
import calendar
print(calendar.month(2025, 4))
```

---

## 📂 Project Structure
```
📦 Python_Lessons
 ┣ 📜 control_modules_functions.py
 ┣ 📜 exception_handling.py
 ┣ 📜 file_handling.py
 ┣ 📜 math_datetime_calendar.py
 ┗ 📜 README.md  # This file
```

---

## 📢 Contributing
Feel free to contribute by adding more examples, improving explanations, or suggesting new topics!

---

## 📜 License
This repository is open-source and available for educational purposes.

