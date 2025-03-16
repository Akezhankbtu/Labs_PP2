n=int(input("Number:"))
def down(n):
    for i in range(n,-1,-1):
        
        yield i
for num in down(n):
    print(num)