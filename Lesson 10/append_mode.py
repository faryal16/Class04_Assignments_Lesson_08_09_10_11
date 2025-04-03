import os

file_folder = "Lesson 10"
file_name = "example_write.txt"
file_path = os.path.join(file_folder, file_name)

with open(file_path, 'a') as file:
    file.write("Appending this line to the file.\n")
    file.write("Appending this line to the example_write.txt file.\n")
    print("Append Mode: Opening 'example_append.txt' in append mode")
    print("Append Mode: Data has been added to 'example_append.txt'.")
