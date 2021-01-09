import glob

import pandas as pd

# read CVS files from the dedicated folder and concatenate them into one df

path = r'c:\\Users\szere\OneDrive\Pulpit\kody Python\Python Stock Data'
all_files = glob.glob( path + "/*stock*.csv" )

li = []

for filename in all_files:
    df = pd.read_csv( filename, index_col=None, header=0 )
    li.append( df )

data = pd.concat( li, axis=0, ignore_index=True )
print ( data )

# add a new column with % calculations

data2 = data
data2['Change %'] = (data.Close - data.Open) / data.Open * 100

print( data2 )

df = data2
df.to_csv( r'C:\\Users\szere\OneDrive\Pulpit\kody Python\Python Stock Data\All stock rates.csv', index=False,
           header=True )