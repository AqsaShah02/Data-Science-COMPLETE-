import os

# Target directory
target_dir = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 4"

# Step 1: Delete old files from current script folder
for i in range(1, 51):
    file_name = f"{i}.py"
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name} from current folder")

# Step 2: Create files in target folder
questions = [
    "Q1. Write a Python program to check if a string has all unique characters.",
    "Q2. Create a program that removes all duplicate characters from a string.",
    "Q3. Write a script to count the frequency of each character in a string.",
    "Q4. Write a program that accepts a sentence and calculates the number of upper and lower case letters.",
    "Q5. Create a program to find the longest word in a sentence.",
    "Q6. Write a program that takes a string and returns the string in reverse order without using [::-1].",
    "Q7. Create a Python function to check if a string is a pangram.",
    "Q8. Write a Python script to sort words in a sentence alphabetically.",
    "Q9. Write a program to check if two strings are anagrams.",
    "Q10. Write a Python program to capitalize the first letter of each word in a sentence.",
    "Q11. Create a program that extracts numbers from a string and returns their sum.",
    "Q12. Write a program to replace all spaces in a string with underscores.",
    "Q13. Write a function to count how many times a substring appears in a string.",
    "Q14. Write a script to convert a string into title case without using .title().",
    "Q15. Write a Python program to merge two dictionaries into one.",
    "Q16. Create a program to filter out all non-alphabetic characters from a string.",
    "Q17. Write a function that returns True if a string ends with a given suffix.",
    "Q18. Create a program that counts words, characters, and lines in a paragraph.",
    "Q19. Write a script to encode a string using Caesar cipher (shift = 3).",
    "Q20. Write a program that accepts a string and counts vowels and consonants.",
    "Q21. Create a script to convert binary string to decimal.",
    "Q22. Write a program to count the number of words starting with a vowel in a string.",
    "Q23. Create a script that takes a sentence and removes all stop words.",
    "Q24. Write a Python program to split a sentence into words and reverse each word.",
    "Q25. Write a function that returns a new string made of every third character of the original string.",
    "Q26. Write a program to find all palindromic substrings in a string.",
    "Q27. Write a function that compresses a string using run-length encoding.",
    "Q28. Write a Python program to count the frequency of each word in a file.",
    "Q29. Write a script that extracts hashtags from a tweet.",
    "Q30. Write a function to remove punctuation from a string.",
    "Q31. Create a program that finds the first non-repeating character in a string.",
    "Q32. Write a script that converts camelCase to snake_case.",
    "Q33. Write a function to generate acronyms from a sentence.",
    "Q34. Write a script to check if a file contains a specific word.",
    "Q35. Write a Python program to find and replace text in a file.",
    "Q36. Write a script that checks if all characters in a string are digits.",
    "Q37. Write a program to calculate the average word length in a sentence.",
    "Q38. Create a function that removes all HTML tags from a string.",
    "Q39. Write a program to parse a date string and display it in a different format.",
    "Q40. Write a script that finds all email addresses in a given text.",
    "Q41. Write a program that counts the occurrence of each vowel in a paragraph.",
    "Q42. Create a function that validates an email address format.",
    "Q43. Write a script to check if a string is a valid URL.",
    "Q44. Write a program that extracts all integers from a given text.",
    "Q45. Create a script to find duplicate words in a paragraph.",
    "Q46. Write a program that converts a sentence to Pig Latin.",
    "Q47. Write a script that finds the longest sentence in a paragraph.",
    "Q48. Write a Python program to read a file and display all lines that contain a given keyword.",
    "Q49. Write a script to clean a text file by removing extra spaces and blank lines.",
    "Q50. Write a Python program to count how many sentences are in a paragraph."
]


# Ensure target directory exists
os.makedirs(target_dir, exist_ok=True)

# Create files in target directory
for i, q in enumerate(questions, start=1):
    file_path = os.path.join(target_dir, f"{i}.py")
    with open(file_path, "w") as f:
        f.write(f"# {q}\n")
    print(f"Created {file_path}")
