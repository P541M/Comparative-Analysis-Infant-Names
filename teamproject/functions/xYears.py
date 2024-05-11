#!/usr/bin/env python3

import pandas as pd

def xYears():
  
    # User input for year 
    year = input("Year that you would like to search: ")

    df = pd.read_csv('sortedMaleCali.csv')

    df = df.loc[df['Year'] == int(year)]

    # Total number of names for X year 
    total = df.Count.sum()

    # Final function print statement 
    print("There are " + str(total) + " names on the file for the year " + year)