import os

file_name = 'test.txt'
current_directory = os.getcwd()
file_path = os.path.join(current_directory, file_name)
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        line_count = 0
        for line in file:
            line_count += 1
    print(f"Number of lines in the file: {line_count}")
else:
    print("Error: File not found.")
