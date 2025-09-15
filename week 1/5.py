# Q5. Write a program to find the largest of three numbers.

a = int (input("enter any number"))

b = int (input("enter any number"))

c = int (input("enter any number"))

if a>b and a>c:
    print("the largest number is :",a)
elif b>c:
    print("the largest number is :",b)
else:
    print("the largest number is :",c)