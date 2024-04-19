# pands-weeklytasks

**by Grainne Boyle**

I work at [TE Connectivity] (https://www.te.com/usa-en/home.html)

I am a student at the [Atlantic Technological University] (https://www.atu.ie/), Galway, studying the Higher Diploma in Science in Data Analytics on a part-time basis over 2 years.

This Read Me file is for the Programming and Scripting Year 1 module . It describes the weekly tasks and explains how I solved them and what research I did . I include reference resources that I used to come to the solution.

I do not have previous coding experience. This first semester has been challenging while I learn completely new topics, work full-time and manage life in general.

Contents:

1 Bank.py Week 2
Task Description:
Write a program called bank.py 
The program should:
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

Solution:
The program is taking user input, performing a simple calculation and displaying the result in a readable format.
The user is prompted to enter the first amount using the input() function, it converts the input to a floating-point number.
Then the user is prompted to enter the second amount  and this is also converted to a floating- point number.
It calculates the sum of these two amounts and stores the result in the variable {answer}.
It prints out the sum in a formatted string using an f-string, where the answer is replaced by the actual sum calculated, and the sum is preceded by the Euro symbol, indicating a monetary amount. I learned how to add the Euro symbol by reading through text on the discord channel.

Accounts.py Week 3

Task description:
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other characters replaced with Xs).
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Solution:
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


Collatz.py Week 4
Task Description: 
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

Solution:
The program is set up to perform the collatz sequence on a positive integer entered by the user. It prompts the user to enter a positive integer.
The while loop is set up until the number reaches the number to end which is 1.
Within the loop, the if statement checks if the current number is even, if it is , it divides the number 2.
The else statement work on the premise that if it is not even, it must be odd, so it multiplies it by 3 and adds 1.
After each calculation, it prints the updated value of the number,
The loop continues until the current number equals 1, and then the loop ends.

References:
To understand the collatz sequence, I watched the you tube video:
[You Tube](https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s)
I also read this article:
[How Stuff works](https://science.howstuffworks.com/math-concepts/collatz-conjecture.htm#:~:text=The%20Collatz%20Conjecture%2C%20also%20known,lead%20to%20the%20number%20one)
To help understand while loops:
[W3 Schools](https://www.w3schools.com/python/python_while_loops.asp)
To help understand if statements:
[Real Python](https://realpython.com/python-conditional-statements/)


weekday.py Week 5
Task Description:
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
You will need to search the web to find how you work out what day it is.

Solution:
The program  imports the datetime module and date and this gives the current date.
It then stores today’s date in the variable today. It prints today’s date using the print function.
Day 0 is considered Monday and Day 6 is considered Sunday.
Using an ‘if’ statement , it checks if it is a weekday. Days 0 to 4 are weekdays so anything under 5, is considered a weekday. If it returns a value less than 5, it means it’s a weekday and prints a message to that effect.
Using an ‘Elif” statement, it checks if it is day 5 or 6, this is considered the weekend and it prints a message indicating it is the weekend.

References:
[She Codes](https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python) This website shows very clearly what you need to import to run the program and print out a result)
[Python calendar](https://docs.python.org/3/library/calendar.html) Define days of the week
[W3 Schools](https://www.w3schools.com/python/gloss_python_elif.asp) If previous conditions do not work, use this condtion.

squareroot.py Week 6
Task description:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.

Solution:
The program prompts the user to input the number they want to find the square root of ‘n’ and their guess for the square root ‘x’ . Both inputs are converted to floating-point numbers using the float function. It prints the initial approximation of the square root. It uses a for loop function and iterates by improving and refining each time until satisfied with the approximation of the square root. It prints the final approximation and has rounded this for simplification.


References:
[Geeks for Geeks](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) helped me to come up with the formula
[You Tube](https://www.youtube.com/watch?v=FpOEx6zFf1o) Explains simply how it works
[Real Python](https://realpython.com/python-for-loop/) Understanding iterations and for loops

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
To help with understanding the function I used Chatgpt to explain what the program was supposed to output


