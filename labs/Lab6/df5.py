import os
file_name = 'output.txt'
file_path = os.path.join(os.getcwd(), file_name)

items = ["Apple", "Banana", "Cherry"]

with open(file_path, "w") as file:
    for item in items:
        file.write(item + "\n")
print(f"List to {file_path}")
