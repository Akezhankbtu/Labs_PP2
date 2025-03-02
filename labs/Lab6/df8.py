import os

file_path = input("Enter: ")

if os.path.exists(file_path) and os.path.isfile(file_path):
    os.remove(file_path)
    print("File deleted")
else:
    print("Error: File does not exist")