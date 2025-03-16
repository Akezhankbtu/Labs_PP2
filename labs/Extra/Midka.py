import os
file_name="test_dir"
#os.mkdir(file_name)
if os.path.exists(file_name):
    print("exist")
else:
    print("no")