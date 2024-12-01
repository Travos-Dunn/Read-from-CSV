# Reading CSV from file
import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row) # each row is a List of strings
