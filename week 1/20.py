# Q20. Create a program to find the second largest number in a list.

numbers = [int(x) for x in input ("enter numbers seprated by commas").split(",")]

if len(numbers) < 2:
    print("the list should contain atlest two numbers")

else :
    first = second = float('-inf') # assigning both variables with smallest possible number minus infinity so that any real number will be greater

    for num in numbers:
        if num>first:
            second =first
            first= num
        elif num >second and num != first:
            second = num

print("the second largest number is ", second)