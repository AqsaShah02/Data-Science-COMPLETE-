# Q1. Write a Python program to check if a string has all unique characters.
def has_unique_chars(s):
    return len(set(s)) == len(s)

# Example
string = "abcdef"
print("Unique:", has_unique_chars(string))   # True
string = "hello"
print("Unique:", has_unique_chars(string))   # False
