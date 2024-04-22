# ES.py
# Week 7

# Program takes in a text file and reads it and counts the number of E's in the file
# author Grainne Boyle

# the program takes the filename from an argument on the command line
import sys

#daffodils = "daffodils.txt";
text_path = sys.argv[1]
# with statement closes resource after processing them.
# in the statement below, open() opens the file, the 'r' represents read
# and the f represents the file object
with open(text_path, 'r') as f: 
    text_path = f.read() 
    # Read the file into a string above
    count = text_path.count('e')
    # to count the amount of times the letter 'e' appears in the file I used the count function
# Print the count
print('The number of es in your document is', (count))

# I changed the program so that it could read in any text file
# You can test it by entering the file name python es.py daffodils.txt
