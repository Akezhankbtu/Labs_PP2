with open('intput.txt', 'r') as file:
    text = file.read().strip()

words = text.split('_')
camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

print("CamelCase результат:")
print(camel_case)
