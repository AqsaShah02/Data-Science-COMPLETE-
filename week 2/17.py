# 17. Write a function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

# Example
print("Vowels in 'Hello World':", count_vowels("Hello World"))