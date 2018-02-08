# imports
import os
import csv

# set csv path
path = os.path.join('Election_Data', 'election_data_1.csv')

with open(path, newline = '') as file:

    # create reader
    reader = csv.reader(file, delimiter = ',')

    # sets loop to start at row 2 to avoid headers
    next(reader)

    # create and initialize variables
    majority = 0
    winner = ""

    # create and initialize lists
    votes = []
    candidates = []

    # fill the lists
    for row in reader:
        if row[2] not in candidates:
            candidates.append(row[2])
        votes.append(row[2])

    # print results
    print("Election Results")
    print("================================")
    print("Total Votes: " + str(len(votes)))
    print("================================")


    for candidate in candidates:
        # calculate %
        percentage = (votes.count(candidate) / len(votes))

        # print candidate with corresponding results
        print(candidate + ": " + "{:.1%}".format(percentage) + " (" + str(votes.count(candidate)) + ")")

        # check for new winner
        if majority < votes.count(candidate):
            majority = votes.count(candidate)
            winner = candidate

    # print winner
    print("================================")
    print("Winner: " + winner)
    print("================================")

    # write results to file
    f = open("Election_Results.txt", "w+")
    f.write("Election Results\n")
    f.write("================================\n")
    f.write("Total Votes: " + str(len(votes)) + "\n")
    f.write("================================\n")

    for candidate in candidates:
        # calculate %
        percentage = (votes.count(candidate) / len(votes))

        # print candidate with corresponding results
        f.write(candidate + ": " + "{:.1%}".format(percentage) + " (" + str(votes.count(candidate)) + ")\n")

        # check for new winner
        if majority < votes.count(candidate):
            majority = votes.count(candidate)
            winner = candidate

    f.write("================================\n")
    f.write("Winner: " + winner + "\n")
    f.write("================================")
    f.close()