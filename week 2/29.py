# 29. Write a function to merge two dictionaries and handle key collisions by summing values.

def merge_dict(dict1,dict2):
    copyy = dict1.copy()
    for key,value in dict2.items():
        if key in copyy:
            copyy[key] += value
        else:
            copyy[key] =value
    return copyy

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}

print(merge_dict(d1, d2))
