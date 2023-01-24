import csv

with open('data1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)


id_list = []