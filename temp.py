# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import pandas as pd
import numpy as np

df = pd.read_csv('angles_UCI_CS.csv')
df[' angle_cosine']=np.cos(df[' angle_degrees'])
#this is another method to apply an extra column in output csv
#df.loc[:,' angle_cosine'] = df.loc[:,' angle_degrees'].apply(lambda x: math.cos(x*math.pi/180))
df.to_csv('out.csv',index=False)

