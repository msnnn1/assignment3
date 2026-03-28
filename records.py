'''
Program to read records.csv and display contents
'''

import csv

with open("records.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)