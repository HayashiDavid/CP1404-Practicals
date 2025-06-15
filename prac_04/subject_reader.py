"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    records = get_data()



def get_data():
    """Read the data file: subject, lecturer, number of students..."""
    input_file = open(FILENAME)
    data = input_file.readline()
    input_file.close()
    return data

def print_data(records):
    """ Print the datas """
    datasets = []
    for line in records:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        datasets.append(parts)
    return  datasets


main()