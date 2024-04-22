# Square root
# Program takes a positive floating-point number as input and outputs an approximation of its square root.

# author Grainne Boyle
"""
# First how do you use python to calculate the square root of a number

I was just testing how it works below using math 
import math

num = float(input("Please enter a positive number: "))

# Calculate the square root
sqrt = math.sqrt(num)

# Print the result
print("The square root of", num, "is", sqrt)
"""
# Using the newton method
# 
# squareroot= 0.5 * (x+n/x) where x is any guess which be assumed to be squareroot of N.  Researched newton method on geeksforgeeks.org
# Write a program to guess the square root number and reiterate until which you get it within a certain tolerance
# Also reviewed different methods on stack overflow, tried a few different methods and change in the final week as I had not set up the function


n = float(input('what number would you like to find the square root of?  '))
x = float(input('Estimate your number  '))

def sqrt(n,x):


    root =(0.5*(x+(n/x)))
    print (root)
    # the i in range iterates between 0 and 5
    for i in range(0,5):
        root = (0.5*(root+(n/root)))
  
        print (round( root,5)) 

    return((round(root,5)))

print('The square root of your number is', sqrt(n,x))

       
