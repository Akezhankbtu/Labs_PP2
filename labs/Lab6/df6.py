import os

current_directory = os.getcwd()
for i in range(26):
    file_name = f"{chr(65 + i)}.txt"
    file_path = os.path.join(current_directory, file_name)
    with open(file_path, "w") as file:
        file.write(f"This is {file_name}\n")
print("26 text files have been created.")