import os

file_folder = "Lesson 10"
file_name = "example_exclusive.txt"
file_path = os.path.join(file_folder, file_name)

try:
    with open(file_path, 'x') as file:
        file.write("This file is created using exclusive mode.\n")
        print("Exclusive Mode: Attempting to create 'example_exclusive.txt'")
        print("Exclusive Mode: 'example_exclusive.txt' created successfully.")
except FileExistsError:
    print("Exclusive Mode: 'example_exclusive.txt' already exists.")