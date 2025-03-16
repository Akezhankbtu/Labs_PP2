def is_even(x):
    return x%2==0
def square(x):
    return x**2
numbers=list(map(int,input().split()))
even_numbers=filter(is_even,numbers)
squared_nums=map(square,even_numbers)
print(list(squared_nums))