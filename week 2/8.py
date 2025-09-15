# 8. Write a program to merge two dictionaries.


# A dictionary in Python stores data as key–value pairs.

# Example:

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

dict1 = {"name": "Aqsa", "age": 21}
dict2 = {"city": "Mumbai", "course": "ECS"}


d2 ={**dict2,**dict1}

print("Using unpacking:", d2)

#  Method 2
# d1 = dict1.copy()
# d1.update(dict2)
# print("Using update():", d1)

#method 3
# d3 = dict1 | dict2
# print("Using | operator:", d3)