# Q8. Create a program to count the number of vowels in a string.

ask = input("enter a string:").lower()

vowels = "aeiou"
count = 0
for char in ask:
    if char in vowels:
        count +=1

print (f"number of vowels in {ask} is {count}")