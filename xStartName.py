import pandas as pd
import sys

def userSelectionStartName():

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

    print("Enter a letter to find the names that start with that letter: ", end = ' ')
    letter = input().lower()
  
    #function calls
    if locationChoice == 'a':
        australia(genderChoice, letter)
    elif locationChoice == "A":
        australia(genderChoice, letter)
    if locationChoice == 'c':
        california(genderChoice, letter)
    elif locationChoice == 'C':
        california(genderChoice, letter)




#function for australia
def australia(genderChoice, letter):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("Male names that start with", letter, "are:", ", ".join(names))
        else:
            #will print this if there were none found
            print("No male names were found that start with", letter)
    elif(genderChoice == "M"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedMaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("Male names that start with", letter, "are:", ", ".join(names))
        else:
            #will print this if there were none found
            print("No male names were found that start with", letter)

    
    
    #if statement to validate the input for females (f/F)
    if(genderChoice == "f"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("Female names that start with", letter, "are:", ", ".join(names))
        else:
            #will print this if there were none found
            print("No female names were found that start with", letter)
    elif(genderChoice == "F"):
        #reads the CSV file from the given directory
        df = pd.read_csv("sortedFiles/sortedFemaleAus.csv")
        
        #goes through the df and filters it depending on the condititon (the letter)
        df = df[df['Name'].str.startswith(letter, na=False)]
        
        #creates a list on the names that meet the condition
        names = list(df["Name"].unique())
        
        #prints the results
        if len(names) > 0:
            print("Female names that start with", letter, "are:", ", ".join(names))
        else:
            #will print this if there were none found
            print("No female names were found that start with", letter)




#function for california, the same concept as above. 
#Only changed the file it was reading and function call name.
def california(genderChoice, letter):

    #if statement to validate the input for males (m/M)
    if(genderChoice == "m"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
        if len(names) > 0:
            print("Male names that start with", letter, "are:", ", ".join(names))
        else:
            print("No male names were found that start with", letter)
    elif(genderChoice == "M"):
        df = pd.read_csv("sortedFiles/sortedMaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
        if len(names) > 0:
            print("Male names that start with", letter, "are:", ", ".join(names))
        else:
            print("No male names were found that start with", letter)

    
    
    #if statement to validate the input for males (f/F)
    if(genderChoice == "f"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
        if len(names) > 0:
            print("Female names that start with", letter, "are:", ", ".join(names))
        else:
            print("No female names were found that start with", letter)
    elif(genderChoice == "F"):
        df = pd.read_csv("sortedFiles/sortedFemaleCali.csv")
        df = df[df['Name'].str.startswith(letter, na=False)]
        names = list(df["Name"].unique())
        if len(names) > 0:
            print("Female names that start with", letter, "are:", ", ".join(names))
        else:
            print("No female names were found that start with", letter)