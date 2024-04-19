# accounts.py  
# Week 3
# Program reads in a 10 character number and outputs the number with only the last four digits showing
# author Grainne Boyle


inputstring=input("please enter a ten digit number: ")

astring = ("XXXXXX")

print ("The account number is: ", astring+inputstring[6:10],)

#I used W3 schools to understand how to slice a string 
#[W3 Schools](https://www.w3schools.com/python/gloss_python_string_slice.asp)
#To concatenate - I did not know how to join the 'X's' and the sliced string together, I used W3 schools to understand this.
#[W3 Schools](https://www.w3schools.com/python/python_strings_concatenate.asp)
       