FILENAME = "wimbledon.csv"
CHAMPIONS = 2
COUNTRIES = 1


def main():
    records = get_records(FILENAME)
    champion_to_wins, countries = display_wins(records)
    display_records(champion_to_wins, countries)


def display_wins(records):
    champion_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRIES])
        try:
            champion_to_wins[record[CHAMPIONS]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPIONS]] = 1
    return champion_to_wins, countries


def display_records(champion_to_wins, countries):
    print("Wimbledon champions: ")
    for name, count in champion_to_wins.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won wimbledon")
    print(",".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            sections = line.strip().split(',')
            records.append(sections)
    return records


main()
