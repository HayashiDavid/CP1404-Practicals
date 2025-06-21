"""
Wimbledon
Estimate: 1 hour
Actual: 50 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    # Read data
    data = read_data("wimbledon.csv")

    # Count champions
    champions = count_champions(data)

    # Get countries
    countries = get_countries(data)

    # Display results
    print("Wimbledon Champions: ")
    for name, wins in champions.items():
        print(f"{name} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def read_data(filename):
    """Read data from file and return list of lists"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            parts = line.strip().split(',')
            data.append(parts)
    return data


def count_champions(data):
    """Count wins for each champion"""
    champions = {}
    for row in data:
        name = row[1]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def get_countries(data):
    """Get unique countries"""
    countries = set()
    for row in data:
        countries.add(row[2])
    return countries



main()