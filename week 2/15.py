# 15. Write a function that returns the factorial of a number.

num = int(input("enter a number"))

def factorial_find(n):
    fact = 1

    for i in range (1, n+1):
        fact *=i

    return fact

print(f"the factorial of {num} is ", factorial_find(num))
