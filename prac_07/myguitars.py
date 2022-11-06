from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    #     get_guitars(FILENAME)
    #     guitars = Guitar()
    get_guitars()
    # guitars = []
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(guitar_to_add)
    #     name = input("Name: ")


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
