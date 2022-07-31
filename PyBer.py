# %%
%matplotlib inline
# %%
import os
import matplotlib.pyplot as plt 
import pandas as pd 
import statistics
import numpy as np 
import scipy.stats as sts 
from matplotlib.ticker import MultipleLocator

import matplotlib as mpl 

# %%
city_file_load = os.path.join('Resources', 'city_data.csv')
ride_file_load = os.path.join('Resources','ride_data.csv')

city_data_df = pd.read_csv(city_file_load)
ride_data_df = pd.read_csv(ride_file_load)
ride_data_df.head()
ride_data_df.dtypes
ride_data_df.info()
city_data_df.info()
# %%
arr_city = city_data_df['city'].unique()
city_list = [name for name in arr_city]
city_list
# %%[markdown]
## inspect and clean datasets
#%%
# Get the unique values of the type of city
#unique() & sum
city_data_df['type'].value_counts()
# or
city_data_df['type'].unique()
sum(city_data_df['type'] == 'Urban')

ride_data_df['city'].value_counts()

# %% [markdown]
## Merge DataFrames
# %%
pyber_data_df = pd.merge(ride_data_df,city_data_df,how = 'left',on=['city','city'])
pyber_data_df.head(10)

# %%
# make sure wether the right dataframe info into marge
city_data_df.loc[(city_data_df['city']=='Lake Jonathanshire')]

# %% [markdown]
## BUBBLE PLOTS
### create each scatter plot individually and add them all to one chart
# %% [markdown]
### Use filter to create 3 new DF for 3 citty types
urban_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Urban')]
rural_cities_df = pyber_data_df.loc[(pyber_data_df['type']=='Rural'),:]
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]

# %%[markdown]
### get x_axis array (the numbers of rides per city per type)
urban_ride_numbers_Series = urban_cities_df.groupby(urban_cities_df['city']).ride_id.count()
rural_ride_numbers_Series = rural_cities_df.groupby(rural_cities_df['city']).ride_id.count()
suburban_ride_numbers_Series = suburban_cities_df.groupby(suburban_cities_df['city']).ride_id.count()

# %% [markdown]
### get y_axis array (the average fare per city per type)
urban_avg_fare_Series = urban_cities_df.groupby(urban_cities_df['city']).fare.agg('mean')
rural_avg_fare_Series = rural_cities_df.groupby(["city"]).mean()["fare"]
suburban_avg_fare_Series =suburban_cities_df.groupby(["city"]).mean()["fare"]

# %% [markdown]
### get markersize array (the average driver per city per type)
urban_avg_driver_Series = urban_cities_df.groupby(urban_cities_df['city']).mean()['driver_count']
rural_avg_driver_Series = rural_cities_df.groupby(rural_cities_df['city']).mean()['driver_count']
suburban_avg_driver_Series = suburban_cities_df.groupby(suburban_cities_df['city']).mean()['driver_count']

# %% [markdown]
### 3 individual scatter plot by MATLAB method then one bubble chart for 3 all cities
### put Series into x-axis and y-axis in scatter() parenthesis, no x=, y=(this is for line)
plt.figure(figsize=(12,7))

plt.scatter(urban_ride_numbers_Series, urban_avg_fare_Series, 
            s=10*urban_avg_driver_Series, c='coral', label ='Urban',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.scatter(rural_ride_numbers_Series, rural_avg_fare_Series, 
            s=10*rural_avg_driver_Series, c='gold', label ='Rural',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.scatter(suburban_ride_numbers_Series, suburban_avg_fare_Series, 
            s=10*suburban_avg_driver_Series, c='skyblue', label ='Suburban',
            alpha=0.8,edgecolors='k', linewidths=1)

plt.xlabel('Total Number of Rides (Per City)', fontsize = 12)
plt.ylabel('Average Fare ($)', fontsize = 12)
plt.title('PyBer Ride-Sharing Data (2019)',fontsize =20)
plt.grid()

plt.text(41,35,'Note:\nCircle size\ncorrelates with\ndriver count per city.', fontsize = '8')
# manual legend's handles size, use attribute: legend.legendHandles[].set_sizes
lgnd = plt.legend(fontsize = '12', loc = 'upper right',scatterpoints=1, 
                   bbox_to_anchor=(1,1), title = 'City Types')
lgnd.get_title().set_fontsize(12)

# -------------------------important ---------------------------------
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]

# save fig first then show() it
plt.savefig('analysis/Fig1.png')

plt.show()

# %% [markdown]
### get statistics infor to show the relevance of data
# use Numpy mean(), median() and SciPy mode()

round(urban_ride_numbers_Series.mean(), 2) 
#print(f'The mode for ride counts for urban trips is {mode_suburban_ride_numbers_Series}')
#print(f"The mean fare price for urban trips is ${mean_urban_fares:.2f}.")
# %% [markdown]
### stats information for ride numbers per city type (without groupby city names)
mean_urban_ride_count = urban_ride_numbers_Series.describe()['mean']
mean_rural_ride_count = rural_ride_numbers_Series.describe()['mean']
mean_suburban_ride_count = suburban_ride_numbers_Series.describe()['mean']

median_urban_ride_count = urban_ride_numbers_Series.describe()['50%']
median_rural_ride_count = rural_ride_numbers_Series.describe()['50%']
median_suburban_ride_count = suburban_ride_numbers_Series.describe()['50%']

mode_urban_ride_count = sts.mode(urban_ride_numbers_Series)
mode_rural_ride_count = sts.mode(rural_ride_numbers_Series)
mode_suburban_ride_count = sts.mode(suburban_ride_numbers_Series)
mode_suburban_ride_count
# %% [markdown]
### stats information for fares per city type (without groupby city names)
#### get orginal dataset 
urban_fares = urban_cities_df['fare'] 
rural_fares = rural_cities_df['fare'] 
suburban_fares = suburban_cities_df['fare'] 

mean_urban_fares = urban_fares.describe()['mean']
mean_rural_fares = rural_fares.describe()['mean']
mean_suburban_fares = suburban_fares.describe()['mean']

median_urban_fares = urban_fares.describe()['50%']
median_rural_fares = rural_fares.describe()['50%']
median_suburban_fares = suburban_fares.describe()['50%']

mode_urban_fares = sts.mode(urban_fares)
mode_rural_fares = sts.mode(rural_fares)
mode_suburban_fares = sts.mode(suburban_fares)
mode_urban_fares
# %%[markdown]
### stats information for driver numbers per city type (without groupby city names)
### which cities need more driver support

urban_drivers = urban_cities_df['driver_count']
rural_drivers = rural_cities_df['driver_count']
suburban_drivers = suburban_cities_df['driver_count']

mean_urban_drivers = urban_drivers.describe()['mean']
mean_rural_drivers = rural_drivers.describe()['mean']
mean_suburban_drivers = suburban_drivers.describe()['mean']
print(f"The mean fare price for urban trips is ${mean_urban_drivers:.2f}.")
print(f"The mean fare price for rural trips is ${mean_rural_drivers:.2f}.")
print(f"The mean fare price for suburban trips is ${mean_suburban_drivers:.2f}.")

median_urban_drivers = urban_drivers.describe()['50%']
median_rural_drivers = rural_drivers.describe()['50%']
median_suburban_driverss = suburban_drivers.describe()['50%']

mode_urban_drivers = sts.mode(urban_drivers)
mode_rural_drivers = sts.mode(rural_drivers)
mode_suburban_drivers = sts.mode(suburban_drivers)


# %%
## TEST-------------------------------------------------------------------------
test_urban_driver = city_data_df.loc[(city_data_df['type']=='Urban'),:]
mean_test_urban = test_urban_driver['driver_count'].mean()
mean_test_urban

test_rural_driver = city_data_df.loc[(city_data_df['type']=='Rural'),:]
mean_test_rural = test_rural_driver['driver_count'].mean()
print(mean_test_rural)

test_suburban_driver = city_data_df.loc[(city_data_df['type']=='Suburban'),:]
mean_test_suburban = test_suburban_driver['driver_count'].mean()
mean_test_suburban
# TEST-----------------------------------------------------------------------------

# %%[markdown]
## BOX_and_Whisker Plot_rides numbers
####There is one outlier in the urban ride count data. 
####The average number of rides in the rural cities is 
####about 4- and 3.5-times lower per city than the urban and suburban cities.
fig, ax = plt.subplots(figsize=(10,6))

ax.boxplot([urban_ride_numbers_Series,rural_ride_numbers_Series,
            suburban_ride_numbers_Series],
            labels = ['Urban', 'Rural','Suburban'], showmeans=True)

ax.set_ylabel('Number of Rides',fontsize=14)
ax.set_xlabel("City Types",fontsize=14)
ax.set_yticks(np.arange(0,45,step = 3.0))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.set_title('Ride Count Data (2019)',fontsize=20)
ax.grid()

plt.savefig('analysis/Fig2.png')
plt.show()

# %%
#TEST-------------------------------------
# ONE FIG 3 AXES
fig,(ax1,ax2,ax3) = plt.subplots(1,3,sharey=True,figsize=(10,10))
ax1.boxplot(urban_ride_numbers_Series,labels = ['Urban'],
            showmeans = True, showfliers = True)
ax2.boxplot(rural_ride_numbers_Series,labels = ['Rural'],
            showmeans = True, showfliers = True)
ax3.boxplot(suburban_ride_numbers_Series,labels = ['Suburban'],
            showmeans = True, showfliers = True)
ax1.set_ylabel('Number of Rides')
ax1.set_title('Ride Count Data (2019)')
ax1.set_xlabel("City Types",fontsize=14)
ax1.grid()
#TEST---------------------------------------------

# %%
# extract the outlier
#urban_city_outlier = urban_ride_numbers_Series.loc[urban_ride_numbers_Series == 39].index[0]
urban_city_outlier = urban_ride_numbers_Series[urban_ride_numbers_Series==39].index[0]
urban_city_outlier
# %%[markdown]
## BOX_and_Whisker Plot_rides numbers
####From the combined box-and-whisker plots, we see that there are no outliers. 
# However, the average fare for rides in the rural cities 
# is about $11 and $5 more per ride than the urban and suburban cities, respectively.

fig, ax = plt.subplots(figsize=(10,6))

ax.boxplot([urban_fares, rural_fares,suburban_fares],
            labels = ['Urban', 'Rural','Suburban'], showmeans=True)

ax.set_ylabel('Fare($USD)',fontsize=14)
ax.set_xlabel("City Types",fontsize=14)
ax.set_yticks(np.arange(0,65,step = 5.0))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.set_title('Ride Fare Data (2019)',fontsize=20)
ax.grid()

plt.savefig('analysis/Fig3.png')
plt.show()


# %%[markdown]
## BOX_and_Whisker Plot_driver count
####The average number of drivers in rural cities is nine to four times
#### less per city than in urban and suburban cities, respectively. 
fig, ax = plt.subplots(figsize=(10,6))

ax.boxplot([urban_drivers, rural_drivers, suburban_drivers],
            labels = ['Urban', 'Rural','Suburban'], showmeans=True)

ax.set_ylabel('Number of Drivers',fontsize=14)
ax.set_xlabel("City Types",fontsize=14)
ax.set_yticks(np.arange(0,75,step = 5.0))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.set_title('Driver Count Data (2019)',fontsize=20)
ax.grid()

plt.savefig('analysis/Fig4.png')
plt.show()

# %%[markdown]
## PIE charts: % of total fare by city types

type_totalFare_Series = pyber_data_df.groupby(pyber_data_df['type']).fare.agg('sum')
all_totalFare = type_totalFare_Series.sum()

urban_fares_percentage = type_totalFare_Series['Urban']/all_totalFare*100
rural_fares_percentage = type_totalFare_Series['Rural']/all_totalFare*100
suburban_fares_percentage = type_totalFare_Series['Suburban']/all_totalFare*100
print(f"Urban is {urban_fares_percentage:.2f}%, Ruran is {rural_fares_percentage:.2f}%, Subrban is {suburban_fares_percentage:.2f}%.")

plt.figure(figsize=(10,6))
plt.pie([urban_fares_percentage,rural_fares_percentage,suburban_fares_percentage],
        labels = ['Urban','Rural','Suburban'], colors= [ "lightcoral","gold","lightskyblue"],
        autopct='%.1f%%',explode=[0.1,0,0],shadow= True, startangle=270)

plt.title(" % of Total Fares by City Type")
# the Pie plot dont have fontsize parameter
# Change the default font size from 10 to 14.
mpl.rcParams['font.size']=16

plt.savefig('analysis/Fig5.png')
plt.show()
# %%[markdown]
## PIE charts: % of total rides by city types
type_totalride_Series = pyber_data_df.groupby(pyber_data_df['type']).ride_id.count()
all_totalride = pyber_data_df['ride_id'].count()

urban_rides_percentage = type_totalride_Series['Urban']/all_totalride*100
rural_rides_percentage = type_totalride_Series['Rural']/all_totalride*100
suburban_rides_percentage = type_totalride_Series['Suburban']/all_totalride*100
print(f"Urban is {urban_rides_percentage:.2f}%, Ruran is {rural_rides_percentage:.2f}%, Subrban is {suburban_rides_percentage:.2f}%.")

plt.figure(figsize=(10,6))
plt.pie([urban_rides_percentage,rural_rides_percentage,suburban_rides_percentage],
        labels = ['Urban','Rural','Suburban'], colors= [ "lightcoral","gold","lightskyblue"],
        autopct='%1.1f%%',explode=[0.1,0,0],shadow= True, startangle=270)

plt.title(" % of Total rides by City Type")

# no need enter again: mpl.rcParams['font.size']=16
plt.savefig('analysis/Fig6.png')
plt.show()


# %% [markdown]
## PIE charts: % of total drivers by city types
### still use merged dataframe
type_totaldriver_Series = pyber_data_df.groupby(pyber_data_df['type']).driver_count.sum()
all_totaldriver = pyber_data_df['driver_count'].sum()

urban_drivers_percentage = type_totaldriver_Series['Urban']/all_totaldriver*100
rural_drivers_percentage = type_totaldriver_Series['Rural']/all_totaldriver*100
suburban_drivers_percentage = type_totaldriver_Series['Suburban']/all_totaldriver*100
print(f"Urban is {urban_drivers_percentage:.2f}%, Ruran is {rural_drivers_percentage:.2f}%, Subrban is {suburban_rides_percentage:.2f}%.")

plt.figure(figsize=(10,6))
plt.pie([urban_drivers_percentage,rural_drivers_percentage,suburban_drivers_percentage],
        labels = ['Urban','Rural','Suburban'], colors= [ "lightcoral","gold","lightskyblue"],
        autopct='%1.1f%%',explode=[0.1,0,0],shadow= True, startangle=200)

plt.title(" % of Total Drivers by City Type")
plt.savefig('analysis/Fig7.png')
plt.show()

# %%