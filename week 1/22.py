# Q22. Create a program to print all Armstrong numbers between 1 to 1000.



for num in range (1,1001):
    length = len(str(abs(num)))
    sum_of_powers = 0
    temp=num

    while temp >0:
        digit= temp%10
        sum_of_powers += digit**length
        temp //=10

    if num == sum_of_powers:
        print(num)

