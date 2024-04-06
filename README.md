# pands-weeklytasks

**by Grainne Boyle**

I work at [TE Connectivity] (https://www.te.com/usa-en/home.html)

I am a student at the [Atlantic Technological University] (https://www.atu.ie/), Galway, studying the Higher Diploma in Science in Data Analytics on a part-time basis over 2 years.

This Read Me file is for the Programming and Scripting Year 1 module . It describes the weekly tasks and explains how I solved them and what research I did . I will also reference resources that I used to come to the solution.

I do not have previous coding experience. This first semester has been challenging while I learn completely new topics, work full-time and manage life in general.

Contents:

1 Bank.py
Task Description:
Write a program called bank.py 
The program should:
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 



The program is taking user input, performing a simple calculation and displaying the result in a readable format.
The user is prompted to enter the first amount using the input() function, it converts the input to a floating-point number.
Then the user is prompted to enter the second amount  and this is also converted to a floating- point number.
It calculates the sum of these two amounts and stores the result in the variable {answer}.
It prints out the sum in a formatted string using an f-string, where the answer is replaced the actual sum calculated, and the sum is preceded by the Euro symbol, indicating a monetary amount. I learned how to add the Euro symbol by reading through text on the discord channel.

2. Accounts.py

Task description:
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

The program is designed to hide sensitive information by revealing only a portion of the acount number, specifically the last four digits. It uses strings , concatenation and slicing.
It prompts the user to input a ten digit number using the input() function and stores in the variable inputstring.
The .astring  creates a string consisting of six ‘X’ characters, which is used to mask the first six digits of the account number and serves as a placeholder for the hidden digits.
A slicing notation is used[6:10] which extracts characters from the end of the input string.
The + operator concatenates astring with the sliced portion of inputstring.
The result is a string that combines the ‘X’s and the last four digits of the account number.
I used W3 schools to understand how to slice a string 
[W3 Schools](https://www.w3schools.com/python/gloss_python_string_slice.asp)
I did not know how to join the 'X's' and the sliced string together, I used W3 schools to understand this.
[W3 Schools](https://www.w3schools.com/python/python_strings_concatenate.asp)







