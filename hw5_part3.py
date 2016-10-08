# File: hw5_part3.py
# Author: Uzoma Uwanamodo
# Date: 10/8/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Print a series of numbers, counting down, replacing certain numbers with a string
# Collaboration:
# I did not collaborate with anyone on this assignment


def main():
    DIVISORS = [30,6,5] # The numbers whose divisiblilty we need to watch out for
    for i in range(101, 0, -1):
        def string(x):
            return {0:"Thirty days hath September.", 1:"I'll believe six impossible things before breakfast.", 2:"Where do you see yourself in five years?"}.get(x, i)
        mods = [i %x for x in DIVISORS] # Whether or not i is divisible by any of the divisors
        string = i if 0 not in mods else string(mods.index(0)) # Get the string, if the number is divisible by any one of the numbers in DIVISORS
        print(string)
main()