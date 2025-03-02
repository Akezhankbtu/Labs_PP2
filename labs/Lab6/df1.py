import os
path=input("enter path:")
if os.path.exists(path):
    items=os.listdir(path)#give all of things in directory
    print("Directories:")
    for item in items:
        if os.path.isdir(os.path.join(path,item)):
            print(item)
    print("\nFiles:")        
    for item in items:
        if os.path.isfile(os.path.join(path,item)):
            print(item)
    print("\nAll items:")
    for item in items:
        print(item)
else:
    print("The specified path does not exist!")

