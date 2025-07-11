""" Project Management file
Estimate: 3 hours
Actual:
"""

import datetime

MENU = """ >>> (L)oad Projects
>>> (S)ave Projects
>>> (D)isplay Projects
>>> (F)ilter Porjects by Date 
>>> (A)dd New Projects
>>> (U)pdate Project
>>> (Q)uit
"""



def main():
    """ Main menu that will run project management"""

    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Choice")
            choice = get_choice()



def get_choice():
    """This function will ask the user for a choice"""
    print(MENU, end="\n")
    choice = input(">>> ").upper()
    return choice
