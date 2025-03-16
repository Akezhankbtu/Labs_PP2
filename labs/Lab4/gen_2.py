def even_generator(n):
    for i in range(0, n + 1, 2):# with 2 steps for add only evens
        yield i
n = int(input("Number: "))

print(",".join(str(num) for num in even_generator(n)))
