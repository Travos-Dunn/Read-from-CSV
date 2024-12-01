# Reading CSV with Headers from file
import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row)                  # each row is an OrderedDict
        print(row["ColumnName"])    # how to access a specific column by its header
