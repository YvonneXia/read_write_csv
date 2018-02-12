# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import math

df = pd.read_csv('/Users/yuanxia/Desktop/angles_UCI_CS.csv', sep=',')
df.loc[:,' angle_cosine'] = df.loc[:,' angle_degrees'].apply(lambda x: math.cos(x*math.pi/180))
df.to_csv('/Users/yuanxia/Desktop/out.csv', sep = ',',index=False)

