# Q6. Use a list comprehension to filter even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension: keep x if x % 2 == 0
evens = [x for x in numbers if x % 2 == 0]

print("Original:", numbers)
print("Even numbers:", evens)