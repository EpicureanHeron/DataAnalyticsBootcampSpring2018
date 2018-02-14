import csv
import os

path = os.path.join('data', 'cereal_bonus.csv')

with open(path, 'r') as cereals:
    reader = csv.reader(cereals, delimiter = ',')

    next(reader)

    for cereal in reader:
        if float(cereal[7]) >= 5:
            print(cereal[0] + ": " + cereal[7])
