# Q13. Write a program to print all prime numbers between 1 and 100.

for num in range (2,101):
    is_prime = True
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
           # print ("The prime numbers in the range 1 to 100 are :", num)
           print(num, end =" ")