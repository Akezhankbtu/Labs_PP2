import re
with open('input.txt', 'r') as file:
    text = file.read()
result = re.sub(r"([A-Z])", r" \1", text)#() захватывают заглавную букву.\1 возвращает её обратно на место.

print("Результат:")
print(result)