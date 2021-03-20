# -*- coding: utf-8 -*-
"""
our good code block goes up here
"""

# Greet the user
print("Hi, I will ask you for a year and then will tell you how many days were in February that year.")

# Ask them for a year, Convert the year to int
year = int(input("Please enter a year: "))
days = 0

# Do the logic
# check for valid year, no year zero
if year > 0:  # valid years
    # year divisible by 4 and by 400, yes leap
    if year % 4 == 0 and year % 400 == 0:
        days = 29
    # year divisible by 4 and 100, NOT leap
    elif year % 4 == 0 and year % 100 == 0:
        days = 28
    # year divisible by 4 and NOT 100, leap
    elif year % 4 == 0 and year % 100 != 0:
        days = 29
    # year not divisible by 4, NOT leap
    else:
        days = 28
    #	Print out the number of days 
    print("Your year was", year, "and it had", days, "days in February.")
else:  # invalid years
    print("That was not a valid year.")
    


