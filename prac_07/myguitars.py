from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    get_guitars()
    add_guitar(FILENAME)


def add_guitar(filename):
    guitars = []
    with open(filename, 'a') as out_file:
        name = input("Name: ")
        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar_to_add = Guitar(name, year, cost)
            guitars.append(guitar_to_add)
            print(guitar_to_add, file=out_file)
            name = input("Name: ")
    return guitars


def get_guitars():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
