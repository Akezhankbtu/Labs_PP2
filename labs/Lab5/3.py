import re
with open('input.txt','r')as file:
    text=file.read()
pattern=r"[a-z]+_[a-z]+"
matches=re.findall(pattern,text)
if matches:
    print("Найденные совпадения:")
    for match in matches:
        print(match)
else:
    print("Совпадений не найдено.")