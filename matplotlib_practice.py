# %%
%matplotlib inline
# %%
import matplotlib.pyplot as plt 

x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

# %%
plt.plot(x_axis, y_axis, linewidth = 3,marker = '*',color = 'red',label='San jose')
plt.xlabel('Date')
plt.xlim('Jan','Dec')
plt.ylim(0,45)
plt.title('PyBer Fare by Month')
plt.legend()
plt.grid()
#plt.show()


# %%
fig, ax = plt.subplots()
ax.plot(x_axis,y_axis, color ='green', marker = 'D', linewidth = 2,label = 'Boston')
ax.plot([20,15,10,30,35,10,15,34,40,10,41,12])
ax.set_title('PyBer Fare by Month')
ax.set_label('hahaha')
ax.set_xlabel('Date')
ax.set_ylabel('Fare($)')
ax.grid()
ax.set_ylim(0,45)
ax.set_facecolor('red')

#ax.get_frame_on()
ax.legend()

#plt.show()

# %%
fig = plt.figure()
ax = fig.add_subplot()
# run now, only a enpty figure 
ax.plot(x_axis,y_axis)

# %%
ax = plt.axes()
ax.plot(x_axis,y_axis)

# %% [markdown]
### BAR CHART___vertical__MATLAB

plt.bar(x_axis,y_axis, color = 'm', align='edge', label = 'Boston')
plt.xlabel('Date')
plt.ylabel('Fare($)')
plt.legend()



# %% [markdown]
### BAR CHART___Horizontal__MATLAB

plt.barh(x_axis,y_axis,color='m',label='Boston')
plt.ylabel('Date')
plt.xlabel('Fare($)')
plt.legend()
plt.title('PyBer Fare by Month')

# ascanding Y axis order
plt.gca().invert_yaxis()

# %% [markdown]
### BAR CHART___Horizontal change parameter___MATLAB

plt.barh(x_axis,[-20,-15,-10,-30,-35,-10,-15,-34,-40,-10,-41,-12],color='black',label='Boston',align='edge')
plt.ylabel('Date')
plt.xlabel('Fare($)')
plt.legend()
plt.title('PyBer Fare by Month')

# ascanding Y axis order
plt.gca().invert_yaxis()



# %% [markdown]
### BAR CHART___vertical__OBJ-oriented
fig, ax = plt.subplots()
ax.bar(x_axis,y_axis,color ='c',label = 'Chicago')



# %%[markdown]
### BAR CHART___horizontal__OBJ-oriented
ax = plt.axes()
ax.barh(x_axis,y_axis,color = 'y')

## ascanding Y axis order
ax.invert_yaxis()


# %% [markdown]
### Scatter__MATLAB
# %%
plt.scatter(y_axis,x_axis,c='r',s=20,label='Chicago')
plt.gca().invert_yaxis()
plt.xlabel('Fare($)')
plt.ylabel('Date')
plt.xlim(0,50)
plt.title('PyBer Fare by Month')
plt.legend()

# %% [markdown]
### bubble chart__MATLAB
# %%
plt.scatter(x_axis,y_axis,s=[i*5 for i in y_axis], c='g')

# %% [markdown]
### Scatter__OBJ-Oriented

fig=plt.figure()
ax = fig.add_subplot()
ax.scatter(y_axis,x_axis,s=[i*5 for i in y_axis],c='skyblue',alpha = 0.8, linewidths= 2, edgecolors='k',label='Boston')
ax.set_xlabel('Fare($)')
ax.set_ylabel('Date')
ax.invert_yaxis()
ax.set_title('PyBer Fare by Month')
ax.set_xlim(right=50)

ax.legend()


# %% [markdown]
### pie__MATLAB

color_list = ["slateblue", "magenta", "lightblue", "green", "yellowgreen", "greenyellow", "yellow", "orange", "gold", "indianred", "tomato", "mistyrose"]
explode_tuple = (0, 0, 0.2, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)

# MATLAB also use plt.subplots() change fig size 

plt.subplots(figsize=(8,8))
#fig, ax = plt.subplots()
#ax.pie()

plt.pie(y_axis,explode=explode_tuple,labels= x_axis,
        colors=color_list,autopct='%.1f%%',shadow=True, 
        startangle=85,counterclock=False)

plt.show()

# %%