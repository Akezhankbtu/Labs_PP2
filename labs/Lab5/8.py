import re
with open('input.txt', 'r') as file:
    text = file.read().strip()
pattern = r'[A-Z][a-z]+|[A-Z]{2,}'
split_text = re.findall(pattern, text)

print("Результат:")
print(split_text)
