# Reading CSV without CSV module
with open("example.csv", mode="r") as file:
    lines = file.readlines()

delimiter = ","
data = [line.strip().split(delimiter) for line in lines]

for row in data:
    print(row)
