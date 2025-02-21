import re
with open('input.txt','r')as file:
    text=file.read()
pattern=r"[ ,.]"
replaced_text = re.sub(pattern, ":", text)
print("Результаты:")
print(replaced_text)