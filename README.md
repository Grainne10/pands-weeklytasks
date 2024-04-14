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
References:
I used W3 schools to understand how to slice a string 
[W3 Schools](https://www.w3schools.com/python/gloss_python_string_slice.asp)
I did not know how to join the 'X's' and the sliced string together, I used W3 schools to understand this.
[W3 Schools](https://www.w3schools.com/python/python_strings_concatenate.asp)



8. plottask.py

Task description:
Write a program called plottask.py that displays:
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

The program is creating a histogram by generating 1000 random values within a normal distribution. By using a mean of five this will be the average value, and setting the standard deviation to 2 means the data points are close to the average(mean).
A histogram is plotted from the generated random data and shows how the numbers are distributed. 
The program then defines a function h(x) = x³  and plots the function on the same graph as the histogram.
Then the plotted graph is saved as a PNG file named 'plot.png'.
Numpy and matplotlib.pyplot had to be imported to do the histogram and use the random number generator.
I found this challenging as the plotted line did not seem to be correlated to the histogram.
References:
To understand how to plot over the histogram: 
https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
To help with understanding the function I used Chatgpt to explain what the program was supposed to outpu


