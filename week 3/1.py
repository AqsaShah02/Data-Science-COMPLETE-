# Q1: Read a file and print its contents

file_name = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 3\sample.txt"

try:
    with open(file_name, "r") as f:
        content = f.read()
        print("File Contents:\n", content)
except FileNotFoundError:
    print("File not found! Please create 'sample.txt' first.")
