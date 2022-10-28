from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)

    guitars = [gibson, another_guitar]
    print(gibson, another_guitar)
    for guitar in guitars:
        if guitar.get_age(age="") > 50:
            print(f"{gibson} - Expected 100. Got", guitar.year)
            print(f"{another_guitar} - Expected 9. Got", guitar.year)
            print(guitar.is_vintage(age=""))

main()
