# 21. Create a list comprehension to get squares of all even numbers in a range.

def square_even(start,end):
    return [x**2 for x in range (start, end+1) if x%2 ==0]

print(square_even(2,999))