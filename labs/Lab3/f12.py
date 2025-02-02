def histogram(arr):
    for i in arr:
        print("*"*i)
n=input("nums:")
mylist=list(map(int,n.split()))
histogram(mylist)