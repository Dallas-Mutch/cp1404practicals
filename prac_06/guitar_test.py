from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        name = input("Name: ")
        print("\n... snip ...")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
            print(f"Guitar{1}: {guitar.name:>10} ({guitar.year}), worth ${guitar.cost:10, .2f}{vintage_string}")

    # print(f"{guitar.name} get_age() - Expected 100. Got", guitar.get_age())
    # print(f"{another_guitar.name} get_age() - Expected 9. Got", another_guitar.get_age())
    # print(f"{guitar.name} get_age() - Expected True. Got", guitar.is_vintage())
    # print(f"{another_guitar.name} get_age() - Expected False. Got", another_guitar.is_vintage())


if __name__ == '__main__':
    main()
