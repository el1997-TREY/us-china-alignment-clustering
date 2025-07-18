# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df =  pd.read_csv('final_final_final_total.csv')

print(df.head(10))

df.columns

# first deal with tthe
df_no_na = df[df["export_China_dependency"]] 

# df. 


