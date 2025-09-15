# 2. Create a list and find the sum of all its elements.

num = list(map(int,filter(None,input("enter numbers seprated by commas").split(",")))) # FILTER HANDLES ANY EXTRA COMMAS IN INPUT

# enter numbers seprated by commas1,,52,63,62,
# the sum of elements is  178

#total = sum(num)
# print(total)

sum = 0
for n in num: #Take each element of the list numbers, one by one, and temporarily store it in the variable n
    sum += n
# means → total = total + num

# First time: total = 0 + 5 = 5

# Second time: total = 5 + 10 = 15

# Third time: total = 15 + 15 = 30

print("the sum of elements is ",sum)
