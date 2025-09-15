# 5. Write a function to reverse a list.


# def reverse_list(lst):
#     return lst[::-1]   # Slice with step -1


# def reverse_list(lst):
#     lst.reverse()   # Modifies the original list
#     return lst


# numbers = [10, 20, 30, 40]
# print("Reversed list:", reverse_list(numbers))


numbers = [10, 20, 30, 40]

def rev(lst):
    reverse_list =[]

    for i in range(len(numbers)-1,-1,-1):
        reverse_list.append(lst[i])

    return reverse_list

numbers = [10, 20, 30, 40]
print("Original list:", numbers)
print("Reversed list:", rev(numbers))