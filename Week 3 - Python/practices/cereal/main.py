import csv
import os

path = os.path.join('data', 'cereal.csv')

with open(path, 'r') as cereals:
    reader = csv.reader(cereals, delimiter = ',')

    for cereal in reader:
        if float(cereal[7]) >= 5:
            print(cereal[0] + ": " + cereal[7])
