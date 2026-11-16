# Reflection 1:
# Python and Excel can both read sales data, calculate totals, and filter rows.
# Python makes repeating the process across many files easier to automate.
# Excel makes quick visual checks, manual edits, and charts easier without code.
#
# Reflection 2:
# A store could log the date, time, and revenue of each nightly sales import.
# Append mode preserves earlier entries instead of replacing them.
# This history helps employees investigate missing runs or unusual totals.

import csv
from datetime import datetime


# Exercise 1: Confirm the file structure.
print("\nEXERCISE 1: Check the file")

with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)

assert header == ["product", "price", "quantity"]
assert len(rows) == 12

print("Header:", header)
print("Number of data rows:", len(rows))


# Exercise 2: Print every raw row, including the header.
print("\nEXERCISE 2: Raw rows")

with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print("All fields read by csv.reader are strings.")


# Exercise 3: Print the header separately.
print("\nEXERCISE 3: Skip the header")

with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)