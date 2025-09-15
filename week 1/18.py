# Q18. Check whether a character is a vowel or consonant.

text = input(" enter a character ").lower()

vowels = "aeiou"

if text in vowels:
    print (f"the {text} is a vowel")
    
else:
    print (f"the {text} is a consonent")