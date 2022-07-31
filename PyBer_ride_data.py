# %%
%matplotlib inline
# %%
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import os
import statistics
# for xticks, we dont use multipleLocator this time, because we already have array-like ticks labels
from matplotlib.ticker import MultipleLocator
# %% [markdown]
### practice _df.plot() directly plot from dataframe from csv file
# %%
file_load = os.path.join('Resources','PyBer_ride_data.csv')

pyber_ride_df = pd.read_csv(file_load)
pyber_ride_df.columns
pyber_ride_df.count()
#pyber_ride_df.describe()
len(pyber_ride_df)

# %%[markdown]
## line plot and xticks locator set from len(-df)
# %%
fig = plt.figure()
# set up x_axies use np.arange(len(_df))
x_axis = np.arange(len(pyber_ride_df))
# transfer np.array into list by list comprenhension
#ticks_locations = [i for i in x_axis]

pyber_ride_df.plot(x='Month', y='Avg. Fare ($USD)')
plt.xticks(x_axis, labels= pyber_ride_df['Month'])

# %% [markdown]
## plot.bar() and errorbar for _df
# %%
# !!!dont make additional subplots!! _df.plot already made a plot!!!
#fig , ax = plt.subplots()
#--------------------------------------------------------
stdev = statistics.stdev(pyber_ride_df['Avg. Fare ($USD)'])
pyber_ride_df.plot.bar(x='Month',y='Avg. Fare ($USD)',yerr =stdev, capsize=5,color = 'skyblue')
plt.title('Month vs Fare')
# rotation is counterwise aginst x axis! like pie's startangle *kwarg
plt.xticks(rotation = 0)


# %%