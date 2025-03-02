import os
# Получаем путь
path = input("Enter the path to check: ")
#существует ли?
if os.path.exists(path):
    print(f"\n Path '{path}' exists.")
    # Проверяем
    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

else:
    print(f"\n Path '{path}' does not exist!")