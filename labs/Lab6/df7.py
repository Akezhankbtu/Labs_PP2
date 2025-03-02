source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line)

print("File copied")
