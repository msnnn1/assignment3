'''
Program to take user input and append to records.csv
'''

import csv

name = input("Enter name: ")
roll = input("Enter roll no: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

with open("records.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, roll, program, year, group])

print("Data added successfully")