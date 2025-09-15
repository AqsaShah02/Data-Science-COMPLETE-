# Q29. Create a program to check whether a number is prime or not.

num = int(input("enter a number"))

if num <= 1:
    print("enter positive integer")

else:
    is_prime = True
    for i in range (2 , int(num**0.5)+1):
        if num %i ==0:
            is_prime = False
            break

    if is_prime:
        print("the number is a prime number")
    else:
        print("the numer is not a prime numer")
