# File: hw5_part1.py
# Author: Uzoma Uwanamodo
# Date: 10/8/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Generate a "modulus table"
# Collaboration:
# I did not collaborate with anyone on this assignment


def main():
    divisor = int(input("Please enter the number to mod by: ")) # Ask the user for the divisor
    dividend = int(input("Please enter how high you'd like to go: ")) # Ask the user for the dividend
    for i in range(dividend + 1):
        print (i, "%", divisor, "=", i % divisor) # Print the table 
        
main()