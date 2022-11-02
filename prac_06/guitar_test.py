from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013)

    print(f"{guitar.name} get_age() - Expected 100. Got", guitar.get_age())
    print(f"{another_guitar} get_age() - Expected 9. Got", another_guitar.get_age())
    print(f"{guitar.name} get_age() - Expected True. Got", guitar.is_vintage())
    print(f"{another_guitar} get_age() - Expected False. Got", another_guitar.is_vintage())


if __name__ == '__main__':
    main()
