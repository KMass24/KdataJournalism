import json
import csv

f1 = open("data/refined_data.csv", "r", encoding="utf-8-sig")
lines = f1.readlines()

headers = lines[0].strip().split(',')

dictionary = []

for line in lines[1:]:
    values = line.strip().split(',')
    row_dict = dict(zip(headers, values))
    dictionary.append(row_dict)

f1.close()

f2 = open("data/refined_data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()