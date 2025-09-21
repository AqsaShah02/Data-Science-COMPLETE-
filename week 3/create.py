import os

# Target directory
target_dir = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 3"

# Step 1: Delete old files from current script folder
for i in range(1, 11):
    file_name = f"{i}.py"
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name} from current folder")

# Step 2: Create files in target folder
questions = [
    "Q1. Write a Python script to read a file and print its contents.",
    "Q2. Create a file and write your name into it.",
    "Q3. Handle a ZeroDivisionError using try-except.",
    "Q4. Write a program to handle file not found error.",
    "Q5. Create a module with a function and import it in another file.",
    "Q6. Use a list comprehension to filter even numbers from a list.",
    "Q7. Write a generator that yields even numbers up to N.",
    "Q8. Create a program to count lines and words in a file.",
    "Q9. Write a program to read a CSV file and print its contents.",
    "Q10. Handle multiple exceptions in a single try block."
]

# Ensure target directory exists
os.makedirs(target_dir, exist_ok=True)

# Create files in target directory
for i, q in enumerate(questions, start=1):
    file_path = os.path.join(target_dir, f"{i}.py")
    with open(file_path, "w") as f:
        f.write(f"# {q}\n")
    print(f"Created {file_path}")
