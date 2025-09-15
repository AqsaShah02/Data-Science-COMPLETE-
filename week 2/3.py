# 3. Write a program to find the maximum and minimum in a list.

numbers = [1,5,3,9,8,6]
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num>maximum:
        maximum = num
    if num<minimum:
        minimum = num

print("the maximum number is", maximum)
print("the minimum number is", minimum)