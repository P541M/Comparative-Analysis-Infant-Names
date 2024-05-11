#!/usr/bin/env python3
# Libraries
import pandas as pd

def userSelectionHowManyNames():

    locationChoices = ['a', 'A', 'c', 'C']
    genderChoices = ['m', 'M', 'f', 'F']

    print("Enter a or A for Australia, c or C for California: ", end = ' ')
    locationChoice = input()
    while locationChoice not in locationChoices:
        print("Invalid choice, Enter a or A for Australia, c or C for California: ", end = ' ')
        locationChoice = input()
    
    print("Enter m or M for Male, f or F for Female: ", end = ' ')
    genderChoice = input()
    while genderChoice not in genderChoices:
        print("Invalid choice, Enter m or M for Male, f or F for Female: ", end = ' ')
        genderChoice = input()
  
    #function calls
    if locationChoice == 'a':
        austrliaHowMany(genderChoice)
    elif locationChoice == "A":
        austrliaHowMany(genderChoice)
    if locationChoice == 'c':
        californiaHowMany(genderChoice)
    elif locationChoice == 'C':
        californiaHowMany(genderChoice)


def austrliaHowMany(genderChoice):

    #male count verified
    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        count = df['Name'].count()
        print("There are ", count, " Australian Male names.")
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        count = df['Name'].count()
        print("There are ", count, " Australian Male names.")

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        count = df['Name'].count()
        print("There are ", count, " Australian Female names.")
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        count = df['Name'].count()
        print("There are ", count, " Australian Female names.")

def californiaHowMany(genderChoice):

    #california count unverified
    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        count = df['Name'].count()
        print("There are ", count, " Californian Male names.")
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        count = df['Name'].count()
        print("There are ", count, " Californian Male names.")

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        count = df['Name'].count()
        print("There are ", count, " Californian Female names.")
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        count = df['Name'].count()
        print("There are ", count, " Californian Female names.")   




