from itertools import permutations 
def generate_permutation():
    x=input("Enter row:")
    p=permutations(x)
    for pr in p:
        print("".join(pr))#join is joins every element to one string."" это типа не добавлять ничего между символами
generate_permutation()

