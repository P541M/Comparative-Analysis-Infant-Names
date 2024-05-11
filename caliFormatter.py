#!/usr/bin/env python3

import pandas as pd


df = pd.read_csv('cali.csv')

df = df.drop(columns = ['Data_Revision_Date'])

df = df.sort_values(['Year','Rank'],ascending = [0,1])

df = df[['Rank','Name','Count','Sex','Year']]

df2 = df.loc[df['Sex'] == 'Male']
df = df.loc[df['Sex'] == 'Female']

df.to_csv('sortedFemaleCali.csv',index = False)
df2.to_csv('sortedMaleCali.csv',index = False)