# 30. Create a function to find unique elements present in only one of two lists.

def unique_elements(lst1,lst2):
    set1,set2 = set(lst1),set(lst2)
    return list((set1-set2)|(set2-set1))

print(unique_elements([1, 2, 3, 4], [3, 4, 5, 6]))



# Convert lists to sets → remove duplicates and allow set operations.

# set1 = {1, 2, 3, 4}

# set2 = {3, 4, 5, 6}

# set1 - set2 → elements in set1 but not in set2.

# {1, 2}

# set2 - set1 → elements in set2 but not in set1.

# {5, 6}

# Union (|) both → {1, 2, 5, 6}

# Convert back to list → [1, 2, 5, 6]