#Name: Daniel Lavdari
#Date: November 25, 2024
# Ask the user for the name of the input file.
# Ask the user for the attribute (column header) to search by.

import pandas as pd

csvFile = input('Enter CSV file name: ')  # Name of the CSV file

try:
    tickets = pd.read_csv(csvFile)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

print("Available attributes (columns) to search by:")
print(list(tickets.columns))

attribute = input("Enter attribute to search by: ")

if attribute not in tickets.columns:
    print("Invalid attribute. Please check the column name and try again.")
    exit()

print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10])

