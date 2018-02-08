import csv
import os
import datetime
# set csv path
path = os.path.join('Employee_Data', 'employee_data1.csv')

# read and gather data from csv
with open(path, 'r', newline = '') as file:

    # create reader
    reader = csv.reader(file, delimiter = ',')
    name_dict = {"emp id" : [],
                 "first name" : [],
                 "last name" : [],
                 "DOB" : [],
                 "SSN" : [],
                 "State" : []}
    # sets loop to start at row 2 to avoid headers
    next(reader)

    for row in reader:
        # get employee id
        name_dict["emp id"].append(row[0])

        # split the name into first and last
        split_name = row[1].split()
        name_dict["first name"].append(split_name[0])
        name_dict["last name"].append(split_name[1])

        # get and format DOB
        DOB = row[2] # grab DOB
        DOB = DOB.split("-") # split by -
        DOB = datetime.date(int(DOB[0]), int(DOB[1]), int(DOB[2])) # create datetime format
        DOB = DOB.strftime("%m/%d/%y") # format into MM/DD/YY format
        name_dict["DOB"].append(DOB) # append to list in dictionary


        # get and format SSN
        SSN = row[3] # get SSN
        SSN = SSN.split("-") # split by -
        SSN[0] = "***" # change first set of numbers to stars
        SSN[1] = "**" # change second set of numbers to stars
        SSN = SSN[0] + "-" + SSN[1] + "-" + SSN[2] # combine the split SSN
        name_dict["SSN"].append(SSN) # append to list in dictionary

        #TODO: get state and change to abbreviation
        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }

        state = row[4] # get state
        state = us_state_abbrev[state] # change to abbreviation
        name_dict["State"].append(state) # append to list in dictionary
# zip the dictionary
zip_dict = zip(*name_dict.values())

# write dictionary to file
with open('Formatted/formatted1.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(name_dict.keys())
    writer.writerows(zip_dict)

