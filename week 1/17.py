# Q17. Write a program to find the LCM of two numbers.

num1 = int (input("enter a number "))
num2 = int (input("enter a number "))

a=num1
b=num2

def gcd(a,b):
    
    while b!=0:
        remainder= a%b
        a=b
        b=remainder
    return a
    
lcm = (num1*num2)// gcd (num1,num2)

print (f"LCM of {num1} and {num2} is {lcm}")