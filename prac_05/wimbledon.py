import csv


def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    champions = get_champions(data)
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    countries = get_countries(data)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_csv(filename):
    """
    Reads a CSV file and returns a list of lists containing the data.

    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = [row for row in reader]
    return data


def get_champions(data):
    """
    Extracts the champions and their corresponding counts from the data.

    """
    champions = {}
    for row in data:
        champion = row[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions


def get_countries(data):
    """
    Extracts the countries of the champions from the data.

    """
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return countries


main()
