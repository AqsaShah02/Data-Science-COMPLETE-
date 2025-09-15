# Q16. Write a program to find the GCD of two numbers.

num1 = int (input("enter a number "))
num2 = int (input("enter a number "))

a=num1
b=num2

while b!=0:
    remainder= a%b
    a=b
    b=remainder

print(f"the GCD of {num1}and {num2} is {a}")


