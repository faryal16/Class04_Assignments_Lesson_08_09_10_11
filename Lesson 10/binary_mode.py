import os

file_folder = "Lesson 10"
file_name = "example_binary.bin"
file_path = os.path.join(file_folder, file_name)



#  Binary mode ('wb' and 'rb') - Working with binary files
binary_data = b"Hello, Binary World!"
with open(file_path, 'wb') as file:
    file.write(binary_data)
    print("Binary Write Mode: Writing binary data to 'example_binary.bin'")
    print("Binary Write Mode: 'example_binary.bin' written successfully.\n")

with open(file_path, 'rb') as file:
    content = file.read()
    print("Binary Read Mode: Attempting to read 'example_binary.bin'")
    print("Binary Read Mode: Contents of 'example_binary.bin':\n")
    print(content)