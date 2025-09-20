# 22. Write a function to check if a string is an anagram.

i1 = input("enter first word")
i2 = input("enter second word")

def is_anagram(str1,str2):
    str1= str1.replace(" ","").lower()
    str2= str2.replace(" ","").lower()

    return sorted(str1) == sorted(str2) # this will return a boolean value i.e true or false

print(is_anagram(i1,i2))


