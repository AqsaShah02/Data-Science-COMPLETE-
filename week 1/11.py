# Q11. Write a program to find the sum of first N natural numbers.


num = int(input("enter a number to get a sum of from 1 to N:"))

count = 0

for i in range (1,num+1):
    count+=i

print(f"the sum of first {num} number is :{count} ")

