def palindrome():
    s = input("Enter a word or phrase: ")  
    s = s.replace(" ", "").lower()  
    if s == s[::-1]:  
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome()
