# 4. Create a program that removes duplicates from a list.

num = [1,8,8,5,6,9,6,3]

unique_list =[]

for n  in num:
    if n not in unique_list:
        unique_list.append(n)

print("the original list is ", num)
print("the unique list is ", unique_list)