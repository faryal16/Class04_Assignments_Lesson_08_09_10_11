import os

# Define the folder and file path
folder_name = "Lesson 10"
file_name = "example.txt"
file_path = os.path.join(folder_name, file_name)

# Ensure the folder exists
os.makedirs(folder_name, exist_ok=True)

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write("\nHello, this is a sample text file.\nPython is reading this file using 'r' mode.")

# Now read the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
