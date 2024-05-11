#!/usr/bin/env python3

#run command: python3 ./main.py -a aus.csv -b cali.csv
# Libraries
import os
import sys
import getopt
import csv
import termios
import pandas as pd
import signal

# Add the parent directory of the current script to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Reading files and functions 
from scriptCalifornia import readFromFile
from scriptAustralia import readFromFile2
from functions.sameName import californiaSameName, australiaSameName
from functions.xLetters import xLetters
from functions.xYears import xYears
from functions.howManyUniqueNames import userSelection
from functions.howManyNames import userSelectionHowManyNames
from functions.popularNames import userSelectionPopularNames
# from functions.graph import printGraph
from functions.xStartName import userSelectionStartName


def main ( argv ):
    
    s = signal.signal(signal.SIGINT, signal.SIG_IGN)
    
    os.system("stty -echo")

    #print(argv)
    if argv != ['-a', 'aus.csv', '-b', 'cali.csv']:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"a:b:",["input="] )
    except getopt.GetoptError:
        print ( "[ERROR] Usage: ./main.py -a <input file name> -b <input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./main.py -a <input file name> -b <input file name>" )
            sys.exit()
        elif opt in ( "-a", "--input1"):
            inputFileName1 = arg #passed into function
        elif opt in ( "-b", "--input2"):
            inputFileName2 = arg #passed into function
            

    readFromFile2(inputFileName1) #function call read from aus.csv 
    readFromFile(inputFileName2) #function call read from cali.csv 

    userChoice = 'y'
    userNumChoice = 0
    
    os.system("stty echo")
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
	
    whileLoopChoices = ['y', 'Y']

    # User input and validation
    while userChoice in whileLoopChoices:
        
        print("Choose a function [1-6]:")
        print("Function 1: Prints the names with a specifed number of characters.")
        print("Function 2: Prints the names in a specified year.")
        print("Function 3: Prints the most popular name in the country/province.")
        print("Function 4: Prints the names that appear in both male and female lists of a country.")
        print("Function 5: Prints the number of Unique names from both male and females.")
        print("Function 6: Prints the total number of names from both male and females.")
        print("Function 7: Prints the names that start with the letter provided by the user.")
        print("Function 11: Print the graph (IN PROGRESS).")

        userNumChoice = input("Enter a value between [1-7] ")
        
        if userNumChoice == '1':
            xLetters()
        elif userNumChoice == '2':
            xYears()
        elif userNumChoice == '3':
            userSelectionPopularNames()
        elif userNumChoice == '4':
            californiaSameName()
            australiaSameName()
        elif userNumChoice == '5':
            userSelection()
        elif userNumChoice == '6':
            userSelectionHowManyNames()
        elif userNumChoice == '7':
            userSelectionStartName()
        else:
            print("Invalid input")
        
        print("Do you want to continue? (Type y or Y for yes, n or N for no):", end = ' ')
        
        userChoice = input()
        
        possibleChoices = ['y', 'Y', 'n', 'N']
        
        while userChoice not in possibleChoices:
            print("Invalid choice, enter choice again (Type y or Y for yes, n or N for no):", end = ' ')
            userChoice = input()

        signal.signal(signal.SIGINT, s)

# This needs to be here
if __name__ == "__main__":
    main ( sys.argv[1:] )
    