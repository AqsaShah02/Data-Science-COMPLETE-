# Q14: Common elements in two lists

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example
l1 = [1, 2, 3, 4, 5,8]
l2 = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(l1, l2))
