## Hw2
import os
import pandas as pd
# working directory
wd = r'/Users/munkhchimegsukhee/Documents/GitHub/Mygit/data'
os.chdir(wd) # set working directory to wd

# import data files
df = pd.read_excel('data.xlsx')
df.columns
pd.set_option('display.max_rows', 100)

df.info()
df.dtypes
df.head() # first 
df.tail() # last # df.tail(3)

# New list for append into df
list = [11, 'Bat', 'Dorj', 'LU05', 25, 3, 1.2, 'M', '2020-01-11  00:00:00', 'left']
 
# using loc methods
df.loc[len(df)] = list
# using iloc
#df.iloc[2] = list
 
# display
df.tail() # last # df.tail(3)