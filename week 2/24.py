# 24. Write a function to flatten a nested list.

lst = [1,5,9,[5,6,5],52,3,6,2,[1,5]]

def flatten_list (x):
    flat = []
    for items in x:
        if isinstance(items,list):
            flat.extend(flatten_list(items))
        else:
            flat.append(items)
    return flat

print(flatten_list(lst))