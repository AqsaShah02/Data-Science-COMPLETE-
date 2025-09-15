# Q21. Write a program to count the number of digits in an integer.
def count(n):
    return len(str(abs(n)))

#or

def count_digits(n):
    n = abs(n) #absolute value of n that enas only number will be cnsiered eg in case of negative sign

    if n ==0:
        return 1
    count = 0
    while n>0:
        n //= 10
        count += 1
    return count

num = int(input("enter a integer"))
print (f"the number of digits in {num} is ",count(num))
