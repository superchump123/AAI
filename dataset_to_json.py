import csv
import json

d = dict()
with open('data/wine_data/winemag-data-130k-v2.csv', 'r', encoding='utf8') as f:
    data = csv.DictReader(f, dialect='excel')
    for i, row in enumerate(data):
        d[i] = row

outfile = open('data/wine_data/wine_dataset1.json', 'x')
json.dump(d, outfile, indent=4)