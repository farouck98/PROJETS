import csv
with open('./exemple.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)