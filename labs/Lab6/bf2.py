st=input("String:")
up=0
lw=0
for i in st:
    if i.isupper():
        up+=1
    elif i.islower():
        lw+=1
print(f'Upper:{up}',f'Lower:{lw}')