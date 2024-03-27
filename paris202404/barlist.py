import csv 
import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np 
import pandas as pd 
         
#%reload_ext autoreload 
#%autoreload 2 
########################
with open("barlist.csv",'r') as location_file:
  df = pd.read_csv(location_file)


#print('hi')
#print(df)
#print(df.index)
#print(df.columns)

for index,row in df.iterrows():
  print('<a href="' + str(row['url']) + '">' + row['Name'] + '(' + str(row['Arrondissement']) + ')' + '</a> - ' + str(row['Address']) + ' | ' + str(row['Address Notes']) + ' | ' + str(row['Notes']) + '<br>')
