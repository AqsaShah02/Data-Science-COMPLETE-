# 20. Write a function to capitalize the first letter of each word in a string.

input = "im a girl named aqsa"



def capitalize_words(s):
    return s.title()

print(capitalize_words("welcome to data science project"))


# Method 2: Manual way
def capitalize_words_manual(s):
    return " ".join(word.capitalize() for word in s.split())

print(capitalize_words_manual("welcome to data science project"))

