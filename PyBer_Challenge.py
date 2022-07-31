# %%
%matplotlib inline
# %%
import os
import matplotlib.pyplot as plt 
import pandas as pd 
import statistics
import numpy as np 
import scipy.stats as sts 

# %%
city_file_load = os.path.join('Resources', 'city_data.csv')
ride_file_load = os.path.join('Resources','ride_data.csv')

city_data_df = pd.read_csv(city_file_load)
ride_data_df = pd.read_csv(ride_file_load)
ride_data_df.info()
# %%
# Merge two raw datasets into one 
pyber_data_df = pd.merge(ride_data_df,city_data_df,how = 'left',on=['city','city'])

pyber_data_df

# %%[markdown]
## Analysis of Summary Table
### Summary Table Description:
# The PyBer_summary_df showcases 5 columns that includes: *Total Rides,Total Drivers,Total Fares,Average Fare per Ride and Average Fare per Driver*.
# For the first 3 columns, Urban cities have highest total numbers of rides, drivers and fares. Rural cities have the lowest total numbers. Suburban is in the middle.
### Summary Table Conclusion:
# However, comparing the average fare per rides between each city type, rural cities have highest average fare per ride than suburban and urban by 
# around four dollars and 10 dollars, respectively.
# For the average fare per driver column, rural cities also perform well than suburban and urban cities by 40% and 230%. 
# The reason is that the rides and drivers count of rural cities, significantly lower than urban and suburban cities.
# It leads to average values greater than urban and suburban.
# %% 
# Create a summary DataFrame
summary_ride_numbers_ds = pyber_data_df.groupby(pyber_data_df['type']).ride_id.count()
summary_drivers_numbers_ds = city_data_df.groupby(city_data_df['type']).sum()['driver_count']
summary_fares_numbers_ds = pyber_data_df.groupby(pyber_data_df['type']).fare.sum()
summary_avg_Fare_per_ride = summary_fares_numbers_ds/summary_ride_numbers_ds
summary_avg_Fare_per_driver =summary_fares_numbers_ds/summary_drivers_numbers_ds

PyBer_summary_df = pd.DataFrame({'Total Rides':summary_ride_numbers_ds.map('{:,.0f}'.format),
            'Total Drivers':summary_drivers_numbers_ds.map('{:,.0f}'.format),
            'Total Fares':summary_fares_numbers_ds.map('${:,.2f}'.format),
            'Average Fare per Ride':summary_avg_Fare_per_ride.map('${:,.2f}'.format),
            'Average Fare per Driver':summary_avg_Fare_per_driver.map('${:,.2f}'.format)})
PyBer_summary_df.index.name = None
PyBer_summary_df


# %%
# Rename columns
newname_pyber_data_df = pyber_data_df.rename(columns = {'city': 'City', 'date':'Date',
                    'fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 
                    'type':'City Type'} )
# Set the index to the Date column, make a copy and drop extra columns
DateAsIndex_newname_pyber_data_df = newname_pyber_data_df.set_index('Date')

fare_pyber_data_df = DateAsIndex_newname_pyber_data_df.copy().drop(columns = ['Ride Id','City','No. Drivers'])

#Set the index to the datetime data type
fare_pyber_data_df_new_index = fare_pyber_data_df.index.astype('datetime64[ns]')
fare_pyber_data_df.index = pd.Index(fare_pyber_data_df_new_index)

fare_pyber_data_df.info()

# %%
# Calculate the total fares by the type of city and date to create a new DataFrame
sum_fare_pyber_data_df = fare_pyber_data_df.groupby(by = ['Date','City Type']).sum()

# Reset the index
reset_sum_fare_pyber_data_df = sum_fare_pyber_data_df.reset_index()
reset_sum_fare_pyber_data_df

# %%
# Create a pivot table and get information of total fares by city type
TotalFare_pivot_df = pd.pivot_table(reset_sum_fare_pyber_data_df, index = 'Date', 
                     values = 'Fare',columns='City Type', aggfunc=np.sum)
TotalFare_pivot_df
# %%
# Create a new DataFrame on a given date
April_TotalFare_pivot_df = TotalFare_pivot_df.loc['2019-01-01':'2019-04-28']

# Create a new DataFrame by resample fuction in weekly bins
weekly_April_TotalFare_pivot_df = April_TotalFare_pivot_df.resample('W-MON').sum()
weekly_April_TotalFare_pivot_df


# %% [markdown]
## Analysis of Multiple-Line Plot
### Multiple-Line Plot Description:
# This multiple-line charts showcases the total fare per city type changes by times. 
# The X axis shows date from 1/1/2019 to 4/28/2019, and total fare in Y axis. 
# In that line chart, Urban cities have highest total fares, Rural cities are 
# lowest. Suburban is in the middle.
### Multiple-Line Plot conclusion:
# Furthermore, the urban's line shows there are several peaks in March and April. At the same time,
# rural shows some correlation to Urban. 
# For example, in the first week of March, urban total fares are over 2,500 dollars, 
# Rural reaches the lowest point, less than 360 dollars.


# %%
# Create a Multiple-Line Plot for Total Fares for Each City Type based on weekly period
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(12,4))
weekly_April_TotalFare_pivot_df.plot(ax = ax)

ax.set_title('Total Fare by City Type')
ax.set_xlabel('Months')
ax.set_ylabel('Fare ($USD)')

ax.legend(loc='center')
plt.savefig('analysis/Challenge_Fig.png')
plt.show()