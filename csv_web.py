# Reading CSV from web
import csv
import requests

url = "https://gist.github.com/netj/8836201/"
response = session.get(url)
response.raise_for_status()

csv_content = response.text.splitlines()
csv_reader = csv.reader(csv_content)

for row in csv_reader:
    print(row)
