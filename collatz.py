#Week4collatz.py  
# Program asks user to read in a positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, if is odd,
# multiply it by three and add one.
# Have the program end if the current value is one.
# author Grainne Boyle

#Use while loop and if else
numberToEnd = 1
number = int(input("please enter a postive integer:"))
while number != numberToEnd: 
        
    if (number % 2) == 0: 
        number = int(number/2)
        print (number)
    # The number changes, if the number continues to be even, it will not move to the next else statement.
    # If it is odd, it will move to the next statement and keep working between the two calculations until it becomes one.
    else:
        #If it is not an even number, then it must be odd, so multiply it by three and add one.
        number = number*3 + 1
        print (number)  
    # once it gets to the number to end and this is 1 , it will stop the while loop.      



           