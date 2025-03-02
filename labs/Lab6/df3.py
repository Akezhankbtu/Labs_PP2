import os

path = input("Enter the path to check: ")

if os.path.exists(path):
    print(f"\nPath '{path}' exists.")

    if os.path.isfile(path):
        filename = os.path.basename(path)
        print(f"Filename: {filename}")
    else:
        print("This is a directory.")

    directory = os.path.dirname(path)
    print(f"Directory: {directory}")

else:
    print(f"\nPath '{path}' does not exist!")
