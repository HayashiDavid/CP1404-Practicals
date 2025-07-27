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
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            pass
        else:
            print("Invalid option")
            print(MENU)
            menu_choice = input(""">>> """).lower()

def display_taxis(taxis):
    """Display taxi from the list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
