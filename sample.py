import pandas as pd
import glob
import matplotlib.pyplot as plt

# merg all data into a single csv

#read csv
df = pd.read_csv("Sales_Data/Sales_April_2019.csv")


# get data file names
path =r'C:\Users\leosa\Desktop\pandas\Sales_Data'
filenames = glob.glob(path + "/*.csv")

dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))
    

# Concatenate all data into one DataFrame
all_data = pd.concat(dfs, ignore_index=True)

all_data.to_csv("all_data.csv", index=False)

#whats the best month for sales? 

#add month column
#all_data['Month'] = all_data['Order Date'].str[0:2] produce errors


#clean up nan in the rows
nan_df =  all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')

#find or and delete it
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

#add mounth column after fixed the errors
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

#after all this: whats the best month for sales
#and how much was earned that month?

#add sales column
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] =  pd.to_numeric(all_data['Price Each'])
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
results = all_data.groupby('Month').sum()
print(results)

#plot with matplot lib

months = range(1, 13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month')
plt.show()

#what city had the highest number of sales