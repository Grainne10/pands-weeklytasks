# ES.py
# Week 7

# Program takes in a text file and reads it and counts the number of E's in the file
# author Grainne Boyle

# the program takes the filename from an argument on the command line
import sys

daffodils = sys.argv[0]
# with statement closes resource after processing them.
# in the statement below, open() opens the file, the 'r' represents read
# and the f represents the file object

with open(daffodils, 'r') as f: 
    daffodils = f.read() 
    # Read the file into a string above
    count = daffodils.count('e')
    # to count the amount of times the letter 'e' appears in the file I used the count function
# Print the count
print('The number of es in your document is', (count))

