# dependencies
import pandas as pd
import matplotlib.pyplot as plt
import os

# grab file paths
city_data_path = os.path.join('Data', 'city_data.csv')
ride_data_path = os.path.join('Data', 'ride_data.csv')

# read csvs
city_data = pd.read_csv(city_data_path)
ride_data = pd.read_csv(ride_data_path)

# create dataframes
city_df = pd.DataFrame(city_data)
ride_df = pd.DataFrame(ride_data)

# add city type to ride dataframe
ride_df['Type'] = city_df['type']

# get total number of rides per city
city_group_df = ride_df.groupby('city').count()
# get average fare per city
city_avg_df = ride_df.groupby('city').mean()

# remove unecessary columns
city_avg_df = city_avg_df.iloc[:, 0]

# convert back to dataframe
city_avg_df = pd.DataFrame(city_avg_df)

# add average fare column to grouped city dataframe
city_group_df['Average Fare'] = city_avg_df['fare']

# rename columns to reflect count
city_group_df = city_group_df.rename(columns={'date' : 'Total Number of Rides'})

# delete unneeded columns
del city_group_df['fare']
del city_group_df['ride_id']

# remove duplicate city and keep the first occurance
city_df = city_df.drop_duplicates(subset='city',keep='first')

# set index to city
city_df.set_index('city', inplace=True)

# add driver count row to grouped df
city_group_df['Driver Count'] = city_df['driver_count']

# initialize lists
x_axis = []
y_axis = []
driver_count = []


# fill lists with data
for index, row in city_group_df.iterrows():
    x_axis.append(row['Total Number of Rides'])
    y_axis.append(row['Average Fare'])
    driver_count.append(row['Driver Count'])

# make bubble chart
plt.scatter(x_axis, y_axis, s=driver_count)
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")
plt.show()