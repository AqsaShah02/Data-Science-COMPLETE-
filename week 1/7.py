# Q7. Write a program to calculate the factorial of a number using a loop.

input= int (input("enter a number:"))
factorial=1
for i in range (1,input+1):
    factorial*=i
print(f"Factorial of {input} is {factorial}")