#Imports
import csv
import os
import random

#Checks if a file exists
csv_file = "passwords.csv"
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        header = ["Site", "Address", "Username", "Password"]
        writer.writerow(header)
        
lowerCASE = "abcdefghijklmnopqrstuvwxyz"
upperCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
intCASE = "1234567890"

#Gathers necessary details for new entry
def createPassword():
    password = "" #Creates empty string for password to be added to
    minlength = False #Creates check for valid data type for minimum characters for password
    specialCASE = ""
    #Checks if minimum characters is not negative or negative
    while minlength == False:
        lengthLOWER = input("Enter the minimum amount of characters needed in the password (Must be atleast 0):\n").strip()
        if lengthLOWER.isalpha():
            pass
        else:
            lengthLOWER = int(lengthLOWER)
            if lengthLOWER < 0:
                print("Invalid choice")
                pass
            else:
                lengthLOWER = int(lengthLOWER)
                minlength = True
    
    #Creates check if maximum characters is less than minimum characters for password
    while True:
        lengthHIGHER = int(input("Enter the maximum amount of characters needed in the password:\n"))
        if lengthHIGHER > lengthLOWER or lengthHIGHER == lengthLOWER:
            break
        else:
            print("Max character limit can't be under minimum character limit")
            continue
    
    #Asks user which special characters are allowed to be used
    while True:
        #Asks user which special characters are allowed to be used
        s = input("Enter a special character that can be used for your password: \n(Type NA or done to exit)\n").strip()
        
        if s.lower() == "na" or s.lower() == "done":
            break
        elif is_only_special_chars(s):
            print("Updated usable special characters")
            specialCASE += s  #Adds special character to specialCASE string
        else:
            print("Invalid choice - must be special characters only")
            continue
    
    #Builds pool of available characters
    char_pool = lowerCASE + upperCASE + intCASE + specialCASE
    
    if not char_pool:  #Handles case where no special chars entered
        char_pool = lowerCASE + upperCASE + intCASE
    
    #Generates random password by randomly selecting from pool
    password = ''.join(random.choice(char_pool) for _ in range(lengthHIGHER))
    
    print("Your randomly generated password is: " + password)
    return(password)
    
def addEntry():
    site = input("Enter site/app you are creating an account in:\n") #Website where you create account
    name = input("Enter your username for the account:\n") #Username
    address = input("Enter your email address associated with that site:\n") #Email address
    password = input("Enter your password for your account:\n") #Password
    entry = []
    entry.append(site)
    entry.append(address)
    entry.append(name)
    entry.append(password)
    with open(csv_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(entry)
    print("Data successfully added!\n")
    

def newEntry():
    site = input("Enter site/app you are creating an account in:\n") #Website where you create account
    name = input("Enter your username for the account:\n") #Username
    address = input("Enter your email address associated with that site:\n") #Email adress
    password = createPassword()
    entry = []
    entry.append(site)
    entry.append(address)
    entry.append(name)
    entry.append(password)
    with open(csv_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(entry)
    print("Data successfully added!\n")
    
'''Needs to be worked on'''
def alterEntry():
    userChoice = input("Which account/site requires changing: \n")
    menuChoice = 0
    menuChoice = int(input("Which credential requires changing?\n1. Site\n2. Address\n3. Name\n4. Password\n5n Exit\n"))
'''Needs to be worked on'''

#Checks if string contains only special characters (no alphanumeric)
def is_only_special_chars(s):
    if not s:  #Empty string
        return False
    return not any(char.isalnum() for char in s)
        
#Menu for user to choose what they want to do
def menu():
    
    while True:
        userChoice = 0
        userChoice = int(input("What would you like to do?\n1. Add an entry: \n2. Create an entry: \n3. Alter an entry: \n4. Generate a random password: \n5. Exit\n"))
        if userChoice == 1:
            addEntry()
        elif userChoice == 2:
            newEntry()
        elif userChoice == 3:
            alterEntry()
        elif userChoice == 4:
            createPassword()
        elif userChoice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again")

menu()
