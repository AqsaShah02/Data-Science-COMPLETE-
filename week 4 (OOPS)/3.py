# Q3. Write a script to count the frequency of each character in a string.

def char_freq(s):
    freq={}
    for char in s:
        freq[char] = freq.get(char,0)+1
    return freq
        

# Explanation:

# We need to count how many times each character occurs in a string.

# Step 1: freq = {} initializes an empty dictionary.

# Step 2: Loop through every character in the string for char in s:

# Step 3: freq.get(char, 0) → looks up the current count of char in the dictionary.

# If the character is not yet in freq, it returns 0.

# Then add +1 to increase the count.

# Step 4: Store this updated value back in the dictionary.

# Example run with "mississippi":

# Start: freq = {}

# 'm' → not present → {'m': 1}

# 'i' → not present → {'m': 1, 'i': 1}

# 's' → not present → {'m': 1, 'i': 1, 's': 1}

# 's' again → increase → {'m': 1, 'i': 1, 's': 2}

# Continue like this…

# Final output: {'m': 1, 'i': 4, 's': 4, 'p': 2} ✅