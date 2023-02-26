# question 2 & 3 
# 2 - estmated global em
import pandas as pd
import numpy as np

df = pd.read_csv('AIRTRANS_C02.csv', low_memory=False)
df1 = df[['LOCATION', 'Value', 'TIME', 'Time']]

# print(df1)

# filter by region
def co2_by_region(region: str):
    result = df1.loc[df1['LOCATION'] == region] # e.g. AUS
    print(type(result))
    print(result.sample(n=10)) # randomly select n rows
    return result

# co2_by_region('AUS')

def co2_by_time_and_region(year, region):
    # result = df1.loc[df1['TIME'] == year] # filter
    # result2 = df1.loc[df1['LOCATION'] == region] # e.g. 2020 (str) # filter
    
    # filt = (df1.loc[df1['TIME'] == year] & (df1.loc[df1['LOCATION'] == region])) 
    filt = ((df1['TIME'] == year) & (df1['LOCATION'] == region)) 

    # concat_filt = pd.concat([df1['TIME']=='2020',df1['LOCATION']== 'AUS']).unique()
    
    # [df1['TIME'] == year].unique()
    
    # print(concat_filt)
    # print(filt)
    # filt2 = (df1['LOCATION'] == region)
    # result3 = df1.loc[filt, 'AUS']
    # print(result3)
    
    # df_new = df1[[['TIME'] == year, ['LOCATION'] == region]]
    
    # print(df_new)
    
    # print(result)
    # print(result2)
    # print(type(result))
    # # print(result.sample(n=10)) # randomly select n rows
    # return result

# co2_by_time_and_region('2020', 'AUS')

co2_by_region('AUS')

# df1.loc[df1['TIME'] == 2020]  

# df1.query('')