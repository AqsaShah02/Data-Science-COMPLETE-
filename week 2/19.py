# 19. Write a function to remove all punctuation from a string.

import string
input = "hello! there ,,,, im a girlll....!!!!"

def remove_punctuation(s):
    return "".join(ch for ch in s if ch not in string.punctuation)

print(remove_punctuation(input))