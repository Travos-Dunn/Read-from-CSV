# Reading CSV without CSV module: complex data
import re

def parse_csv(line):
    # Example Regex to match CSV fields, accounting for quoted values
    pattern = r'(?:^|,)(?:"([^"]*)"|([^,]*))'
    return [match[0] or match[1] for match in re.findall(pattern, line)]

with open("example.csv", mode="r") as file:
    lines = file.readlines()

data = [parse_csv(line.strip()) for line in lines]

for row in data:
    print(row)
