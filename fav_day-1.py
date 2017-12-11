# Created by: Alireza Teimoori
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of enumerated types

from enum import Enum

# an enumerated type of planets

while True:
    Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    try:
        print("Hello!")
        day_selected = int(input('Enter the day # of the week to see its name:  '))
        print(Days[day_selected-1])
        print("Bye!")
        print("\n\n")
    except :
        print("wrong input! Bye!\n\n")
