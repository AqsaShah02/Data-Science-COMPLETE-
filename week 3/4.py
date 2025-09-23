# Q4. Write a program to handle file not found error.
# q4_file_not_found.py

file_name = "example.txt"

try:
    # Try to open the file in read mode
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    # This block runs if the file doesn't exist
    print(f"Error: '{file_name}' not found. Please check the filename or create the file.")
