#!/usr/bin/env python3
# Libraries
import pandas as pd

def userSelection():

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
        austrliaHowManyUnique(genderChoice)
    elif locationChoice == "A":
        austrliaHowManyUnique(genderChoice)
    
    if locationChoice == 'c':
        californiaHowManyUnique(genderChoice)
    elif locationChoice == 'C':
        californiaHowManyUnique(genderChoice)


def austrliaHowManyUnique(genderChoice):

    #male count verified
    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Australian Male names.")
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Australian Male names.")

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Australian Female names.")
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Australian Female names.")

def californiaHowManyUnique(genderChoice):

    #california count unverified
    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Californian Male names.")
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Californian Male names.")

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Californian Female names.")
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        uniqueCount = df['Name'].nunique()
        print("There are ", uniqueCount, " unqiue Californian Female names.")   




