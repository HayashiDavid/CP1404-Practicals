from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "(q)uit, (c)hoose taxi, (d)rive"

def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

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
            if current_taxi:
                current_taxi.start_fare()
                trip_distance = float(input("Drive for how far?>>> "))
                while trip_distance < 0:
                    print("Invalid distance")
                    trip_distance = float(input("Drive for how far?>>> "))
                current_taxi.drive(trip_distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("Please choose a taxi first before consider to drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(""">>> """).lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxi from the list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()