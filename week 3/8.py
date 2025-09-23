# Q8. Create a program to count lines and words in a file.
file_name = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 3\sample.txt"

try:
    with open(file_name,"r", encoding="utf-8")as f:
        lines = f.readlines()
       
    line_count = len(lines)
    word_count = 0

    for line in lines:
        words = line.split()
        word_count += len(words)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
except FileNotFoundError:
    print(f"Error: '{file_name}' not found.")