import os

# Target directory
target_dir = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 3"

# Delete files 1.py to 50.py in target_dir
for i in range(1, 51):
    file_path = os.path.join(target_dir, f"{i}.py")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")
    else:
        print(f"Not found: {file_path}")

print("✅ Cleanup completed!")
