# Q28. Write a program to find the sum of all even numbers in a list.

uinp = input("enter numbers seprated by spaces")

if uinp.strip == "":
    numbers=[]
else:
    numbers=list(map(int, uinp.split()))

sum_even = 0

for num in numbers:
    if num%2 ==0:
        sum_even  += num

if len(numbers)==0:
    print("the list is empty")
elif sum_even == 0:
    print("there are no even numbers in the list")
else:
    print("the sum of even numbers in the list are :", {sum_even})