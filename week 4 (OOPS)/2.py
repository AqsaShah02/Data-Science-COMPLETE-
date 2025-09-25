# Q2. Create a program that removes all duplicate characters from a string.

def remove_dublicates(s):
    result=""
    for char in s:
        if char not in result:
            result += char
    return result

string = "programming"

print(remove_dublicates(string))



# Step-by-step Explanation

# Initialize an empty string result = "".

# This will store the final answer without duplicates.

# Iterate over each character in the given string using for char in s:.

# Check if the character is already present in the result string:

# if char not in result:

# If it is already present, skip it.

# If not, add it to result.

# Return the final string after the loop ends.