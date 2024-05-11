import pandas as pd
import sys

def userSelectionPopularNames():

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
        australia(genderChoice)
    elif locationChoice == "A":
        australia(genderChoice)
    if locationChoice == 'c':
        california(genderChoice)
    elif locationChoice == 'C':
        california(genderChoice)



def australia(genderChoice):

    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])


def california(genderChoice):

    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])

    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df.loc[df['Rank'] == 1]
        df = df.sort_values(['Count'],ascending = False)
        names = list(df["Name"])
        # print(df)
        print("The most popular name is:",names[0])

