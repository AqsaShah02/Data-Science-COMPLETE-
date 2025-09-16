# 16. Create a function that checks whether a string is a palindrome.

text = input("enter a string")

def palindrome_check(n):
    
    if n == n[::-1]:
        print("the given string is a palindrome")
    return n