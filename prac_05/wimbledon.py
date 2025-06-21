"""
Wimbledon
Estimate: 1 hour
Actual: 50 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    # Read data
    data = read_data("wimbledon.csv")




def read_data(filename):
    """Read data from file and return list of lists"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            parts = line.strip().split(',')
            data.append(parts)
    return data





main()