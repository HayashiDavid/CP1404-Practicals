"""
Wimbledon
Estimate: 1 hour
Actual: 50 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    """Read and display champions and winning countries information"""
    # with open(FILENAME, "r", encoding="utf-8-sig") as in file:
        # data = in_file.readlines()
        # champions = extract_data()



def extract_data(data, number):
    """ Get the data and number """
    items = []
    for line in data[1:]:
        items.append(line.strip().split(",")[number])
    return items

