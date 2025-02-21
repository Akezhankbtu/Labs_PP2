import re
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r"(?<=[a-z0-9])([A-Z])"
snake_case = re.sub(pattern, r"_\1", text).lower()

print(snake_case)   
