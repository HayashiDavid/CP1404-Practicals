from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "(q)uit, (c)hoose taxi, (d)rive"

def main():
    total_bill = 0


    print("Let's drive!")
    print(MENU)
    menu_choice = input(""">>> """).lower()

    while menu_choice != "q":
        if menu_choice == "c":
            pass
        elif menu_choice == "d":
            pass
        else:
            print("Invalid option")
            print(MENU)
            menu_choice = input(""">>> """).lower()

