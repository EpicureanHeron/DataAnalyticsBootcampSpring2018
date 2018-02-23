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

# add city type to grouped df
city_group_df['Type'] = city_df['type']

# initialize lists
urban_x = []
urban_y = []
urban_drivers = []
suburban_x = []
suburban_y = []
suburban_drivers = []
rural_x = []
rural_y = []
rural_drivers = []


# fill lists with data
for index, row in city_group_df.iterrows():
    if row['Type'] == 'Suburban':
        suburban_x.append(row['Total Number of Rides'])
        suburban_y.append(row['Average Fare'])
        suburban_drivers.append(row['Driver Count'])
    elif row['Type'] == 'Urban':
        urban_x.append(row['Total Number of Rides'])
        urban_y.append(row['Average Fare'])
        urban_drivers.append(row['Driver Count'])
    elif row['Type'] == 'Rural':
        rural_x.append(row['Total Number of Rides'])
        rural_y.append(row['Average Fare'])
        rural_drivers.append(row['Driver Count'])

# make bubble chart
plt.scatter(suburban_x, suburban_y, s=suburban_drivers, label='Suburban', color='#FFD700', edgecolor='black')
plt.scatter(urban_x, urban_y, s=urban_drivers, label='Urban', color='#87CEFA', edgecolor='black')
plt.scatter(rural_x, rural_y, s=rural_drivers, label='Rural', color='#FF7F50')
plt.title('Pyber Ride Sharing Data (2016)')
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")
plt.legend(title='City Type', loc='Best')
plt.show()
