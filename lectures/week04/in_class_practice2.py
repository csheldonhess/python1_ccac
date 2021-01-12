# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:38:03 2020

@author: coral
"""

print("Hi, I'd like to convert numeric ages to stages of life for you.")
print("I'm going to ask you for a person's age.")

age = float(input("How old is the person (in decimal years, e.g. 3.5)? "))

if age > 150 or age < 0:
    print("This is not a real person's age.")
elif age >= 0 and age <= 1:
    print("This is an infant. A literal baby.")
elif age < 13:
    print("This is a child.")
elif age < 20:
    print("This is a teenager.")
else:
    print("This is an adult.")