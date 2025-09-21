# 27. Write a function to find the missing number from a list of 1 to N.

def missing_numbers(lst,n):
    expected_sum = n * (n+1)//2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

print(missing_numbers([1,2,4,5,6,7,8,9],9))
