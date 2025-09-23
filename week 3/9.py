# Q9. Write a program to read a CSV file and print its contents.
import csv

file_name = r"C:\Users\AQSA SHAH\OneDrive\Desktop\Data science\week 3\data.csv"

try:
    with open(file_name, newline="",encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row) # each row is a list of strings

except FileNotFoundError:
    print("file not found")


# import pandas as pd

# df = pd.read_csv("data.csv")
# print(df)        # pretty tabular print
# print(df.to_dict(orient="records"))  # list of rows as dicts

