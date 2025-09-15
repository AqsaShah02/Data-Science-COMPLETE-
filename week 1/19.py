# Q19. Write a program to calculate the sum of digits of a number.

num = int(input ("enter a number:"))
count = 0
temp = num

while temp > 0:
    last_digit = temp %10
    count = count + last_digit
    temp = temp//10 #removing last digit
   

print (f"the sum of {num} is {count}")