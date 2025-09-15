# Q3. Write a program to check if a number is even or odd.

num = int (input ("enter a number:"))
#yahan int dena compulsory hai kyuki input hamesha as a string return karta hai

if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")