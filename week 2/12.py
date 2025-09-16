# 12. Create a program to check if a key exists in a dictionary.

dict = {"name":"aqsa","age":"21"}

key_check = input ("enter the key yu wants to check")

if key_check in dict:
    print("key exist in the dictonary with the value ", dict[key_check])
else:
    print("invalid key or the key doesnt exist")