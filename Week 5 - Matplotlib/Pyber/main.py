# dependencies
import pandas as pd
import matplotlib as plt
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
del city_group_df['Type']



city_df[city_df.index.duplicated()]

city_group_df['Driver Count'] = city_df['driver_count']


# x_axis =
# y_axis
