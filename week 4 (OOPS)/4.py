# Q4. Write a program that accepts a sentence and calculates the number of upper and lower case letters.

def count_case (sent):
    upper = sum(1 for c in sent if c.isupper())
    lower = sum(1 for c in sent if c.islower())
    return upper , lower


sentence = "Hello World!"
upper, lower = count_case(sentence)
print("Uppercase:", upper)   
print("Lowercase:", lower) 