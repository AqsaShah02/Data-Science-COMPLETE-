# 1. Write a function to check if a number is even.
 
def check_even (n):
    if n%2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

num = int(input("enter a number"))

check_even(num)