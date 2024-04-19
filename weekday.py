# weekday.py  
# Week 5
# Program works out whether the date is a week day or is a day at the weekend.

# author Grainne Boyle

# Firstly import the function for the current date and time.
# Then do an if and elif code to print a statement depending on if it is a weekday or the weekend.

# This function returns the current date and time :
import datetime
# This pulls in todays date :
from datetime import date

today = date.today()
print("Today's date:", today)
if today.weekday() < 5:
   print("Yes, unfortunately today is a weekday")
elif today.weekday() == 5 or today.weekday() == 6:
    print("It is the weekend, Happy Days")
