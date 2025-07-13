from prac_07.guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """ Read guitar data and ask user to add more to the file """




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

main()





