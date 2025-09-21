# 28. Write a program to remove all None values from a list.


def remove_none(lst):
    return [x for x in lst if x is not None]
print(remove_none([1, None, 2, None, 3, 4])) 