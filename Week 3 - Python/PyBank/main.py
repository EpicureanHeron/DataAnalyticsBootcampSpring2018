# imports
import os
import csv
import locale

# set locale settings to US
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

# set csv path
path = os.path.join('Financial_Records', 'budget_data_1.csv')

with open(path, newline = '') as file:

    # create reader
    reader = csv.reader(file, delimiter = ',')

    # sets loop to start at row 2 to avoid headers
    next(reader)

    # create and initialize lists
    dates = []
    l = []

    # fill the lists
    for row in reader:
        dates.append(row[0])
        l.append(int(row[1]))

    # print report
    print("Financial Analysis")
    print("========================================================")
    print("Total Months: " + str(len(l)))
    print("Total Revenue: " + str(locale.currency(sum(l), grouping = True)))
    print("Average Revenue Change: " + str(locale.currency(round(sum(l)/len(l)), grouping = True)))
    print("Greatest Increase in Revenue: " + dates[l.index(max(l))] + ", " + str(locale.currency(max(l), grouping = True)))
    print("Greatest Decrease in Revenue: " + dates[l.index(min(l))] + ", " + str(locale.currency(min(l), grouping = True)))
    print("========================================================")

    # write to file
    f = open("Financial_Analysis.txt", "w+")
    f.write("Financial Analysis\n")
    f.write("========================================================\n")
    f.write("Total Months: " + str(len(l)) + "\n")
    f.write("Total Revenue: " + str(locale.currency(sum(l), grouping=True)) + "\n")
    f.write("Average Revenue Change: " + str(locale.currency(round(sum(l) / len(l)), grouping=True))+ "\n")
    f.write("Greatest Increase in Revenue: " + dates[l.index(max(l))] + ", " + str(locale.currency(max(l), grouping=True))+ "\n")
    f.write("Greatest Decrease in Revenue: " + dates[l.index(min(l))] + ", " + str(locale.currency(min(l), grouping=True))+ "\n")
    f.write("========================================================")
    f.close()