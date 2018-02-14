import os
import csv

path = os.path.join('Netflix', 'netflix_ratings.csv')

video = input("What show or movie are you looking for?: ")

with open(path, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    found = False

    for row in csvreader:
        if row[0] == video:
            print("\n" + row[0] + " is rated " + row[1] + " and has a user score of " + row[6])
            found = True
            break
    if(found == False):
        print("\n" + video + " could not be found in the library")