#!/usr/bin/env python3

#scriptCalifornia.py

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

def readFromFile(inputFileName):

	df = pd.read_csv(inputFileName)

	df = df.drop(columns = ['Data_Revision_Date'])

	df = df.sort_values(['Year','Rank'], ascending = [0,1])

	df = df[['Rank','Name','Count','Sex','Year']]
	
	df['Name']= df['Name'].apply(str.lower)
	
	df2 = df.loc[df['Sex'] == 'Male']
	df = df.loc[df['Sex'] == 'Female']
	
    # Saves the sorted files to a specific directory 
	folder_path = '/home/socs/workdir/Comparative-Analysis-Infant-Names/teamproject/sortedFiles'
	
	# Names the files to be saved 
	file_name1 = 'sortedFemaleCali.csv'
	file_name2 = 'sortedMaleCali.csv'

	# Designates the file path and adds the file name 
	file_path1 = folder_path + file_name1
	file_path2 = folder_path + file_name2

	# Creates the new CSV files at specified folder path 
	df.to_csv(file_path1,index = False)
	df2.to_csv(file_path2,index = False)