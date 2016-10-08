# File: hw5_part4.py
# Author: Uzoma Uwanamodo
# Date: 10/8/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Determine how many times a string occurs in a larger string
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    mainString = input("First (longer) string: ").lower() # Ask user for the main string
    subString = input("Second (shorter) string: ") # Ask user for the substring
    checkStrings = [mainString[i:i+len(subString)] for i in range(len(mainString))] # Get the substrings from the main strings that will be matched against the users' substring
    for i in range(len(checkStrings)):
        if checkStrings[i] == subString.lower():
            print("At index",i,"found a slice of", subString)
            
main()