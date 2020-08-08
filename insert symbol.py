import csv

with open('symbol.csv', newline='',mode='r', encoding='utf-8-sig') as csvfile:
    data = list(csv.reader(csvfile))

print(data)