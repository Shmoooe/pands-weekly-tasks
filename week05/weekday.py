# This program outputs whether or not today is a weekday.
# Author: Joanna K

# Searched w3schools to find how to display the current date in python:
# https://www.w3schools.com/python/python_datetime.asp

import datetime

today = datetime.datetime.now()
# datetime.now() gives you the current date and time.

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Created a list of the weekdays so the program knows which days they are.
if today != weekday:
    print("It is the weekend, yay!")    # If this is true then the program will print this.
else:
    print("Yes, unfortunately today is a weekday.") # If it is false it will print this.





