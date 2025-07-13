from prac_07.guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """ Read guitar data and ask user to add more to the file """
    guitars = read_guitars(FILENAME)
    print(f"Imported {len(guitars)} from {FILENAME}")
    print("My Guitars!! ")

    guitars.sort()
    print(" \nThese are my guitars sorted by year (Oldest >>> Newest")
    display_guitars(guitars)

    write_guitars_to_file(FILENAME, guitars)
    print(f"Added {len(guitars)} guitars to {FILENAME}")


def read_guitars(filename):
    """ Read guitar data from the csv file """
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            for line in in_file:
                line = line.strip()
                if line:
                    parameters = line.split()
                    if len(parameters) == 3:
                        name, year, cost = parameters
                        guitar = Guitar(name, int(year), float(cost))
                        guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found, try again")
    return guitars

def display_guitars(guitars):
    """ Display all guitars in the csv file in a list """
    for index, guitar in enumerate(guitars, 1):
        print(f"Guitar {index}: {guitar}")


def add_guitars():
    """ Add the new guitars from user """
    guitars = []

    name = input("Guitar name>>> ").strip()
    while name != "":
        year = input(get_valid_number("Year>>> "))
        cost = input(get_valid_number("Cost ($) >>> "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"Guitar added>>> {guitar}")

        name = input("Guitar name>>> ").strip()
    return guitars


def get_valid_number(prompt):
    """Validate input to get proper number"""
    is_valid = False

    while not is_valid:
        try:
            number = float(input(prompt))
            if number > 0:
                is_valid = True
            else:
                print("Invalid input! Please enter valid numbers.")
        except ValueError:
            print("Value Error; Please enter a proper number.")
    return number

def write_guitars_to_file(filename, guitars):
    """Write guitars to CSV file"""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()