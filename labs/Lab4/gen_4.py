a=int(input("Number 1:"))
b=int(input("Number 2:"))
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
for num in squares(a,b):
    print(num)