import os

file_folder = "Lesson 10"
file_name = "example_write.txt"
file_path = os.path.join(file_folder, file_name)

with open(file_path, "w") as file:
    file.write("Hello, this is a new file created using write mode\n")
    print("Write Mode: Writing to 'example_write.txt")
    print("Write Mode: File 'example_write.txt' has been created/overwritten.")