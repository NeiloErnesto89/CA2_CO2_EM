import pandas as pd
import numpy as np

#Gathering information from CSV file data in https://stats.oecd.org/Index.aspx?DataSetCode=AIRTRANS_CO2#
df = pd.read_csv('AIRTRANS_CO2_.csv', low_memory=False)
df

#Data to retrieve
df_new = df[['LOCATION', 'Value', 'TIME', 'Time', 'Source of emissions']]
#Get Co2 by region
def get_co2_by_region(region_name):
    
    result = df_new.loc[df_new['LOCATION'] == region_name]
    print(result)

    #Get filter region and year
def get_time_and_region(region_name, year):
    data = df_new.loc[df_new['LOCATION'] == region_name]
    data2 = data.loc[data['TIME'] == year]

    #Filter location and month
def get_month_year_region(region_name, year):
    data = df_new.loc[df_new['LOCATION'] == region_name]
    print(data)
    data2 = data.loc[data['Time'] == year] 
    print(data2)

    #Print region Austrailia in 2020
    get_time_and_region('AUS','2020')
    #Print region USA in December 2022
    get_month_year_region('USA','Dec-22')