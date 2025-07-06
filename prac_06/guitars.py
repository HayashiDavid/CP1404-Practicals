from prac_06.guitar import Guitar

MINIMUM_NUMBER = 0

def main():
    """Ask for guitar details :name, year and cost, until blank is entered then output all details"""
    guitars = []
    print("My guitars!")

    print("There are my guitars: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))



def display_guitars(guitars):
    """Display guitars with a dynamic formatting style """
    # Get formatting widths
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

    # Print each guitar
    for count, guitar in enumerate(guitars, 1):
        is_vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {count}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:>{max_cost_length},.2f}{is_vintage}")


main()