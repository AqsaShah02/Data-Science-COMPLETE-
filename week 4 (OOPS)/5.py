# Q5. Create a program to find the longest word in a sentence.

def longest_word(sent):
    words = sent.split()
    return max(words, key=len)

# Example
sentence = "Python makes programming fun and interesting jadhiweugferfbwejfbawjfbwu"
print("Longest word:", longest_word(sentence))




# Explanation:

# We want to find the word with the maximum length.

# sentence.split() → breaks the sentence into a list of words.
# Example: "Python makes programming fun and interesting" →
# ["Python", "makes", "programming", "fun", "and", "interesting"]

# max(words, key=len) → finds the element with the highest length.

# key=len means the comparison will be based on word length.

# Example run:

# "Python" → length 6

# "makes" → length 5

# "programming" → length 11

# "fun" → length 3

# "and" → length 3

# "interesting" → length 11

# 👉 Two words "programming" and "interesting" both have length 11.
# Python’s max() will return the first one it encounters: "programming".

# ✅ Output → "programming"