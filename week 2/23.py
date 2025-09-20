# 23. Create a nested dictionary to represent student records.

# Nested dictionary for student records
students = {
    "S101": {
        "name": "Aqsa Shah",
        "age": 21,
        "marks": {"Math": 90, "Science": 88, "English": 85}
    },
    "S102": {
        "name": "Rahul Mehta",
        "age": 22,
        "marks": {"Math": 76, "Science": 80, "English": 79}
    },
    "S103": {
        "name": "Sara Khan",
        "age": 20,
        "marks": {"Math": 92, "Science": 95, "English": 89}
    }
}

# Example usage
print(students["S101"])          # full data f that student
print(students["S103"]["marks"]["Math"]) # 92
