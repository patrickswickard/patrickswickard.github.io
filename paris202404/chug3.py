import csv 
import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np 
import pandas as pd 
         
#%reload_ext autoreload 
#%autoreload 2 
########################
with open("gallerylist.csv",'r') as gallery_file:
  df = pd.read_csv(gallery_file)


#print('hi')
#print(df)
print(df.index)
print(df.columns)

for index,row in df.iterrows():
    print('<a href="' + str(row['url']) + '">' + row['Name'] + '</a> - ' + str(row['Address']) + '<br>')
