import os

file_folder = "Lesson 10"
file_name = 'example.txt'
file_path = os.path.join(file_folder, file_name)

#  Update mode ('r+') - Reading and writing to the same file
with open(file_path, 'w') as file:
    file.write("This file will be updated!\n")
    print("Update Mode: Creating 'example_update.txt' and writing initial content\n")

with open(file_path, 'r+') as file:
    print("Update Mode: Attempting to read 'example_update.txt'")
    print("Update Mode: Original Content:\n")
    print(file.read())
    file.write("New content added using update mode.\n")
    print("Update Mode: Writing new content to 'example_update.txt'")
