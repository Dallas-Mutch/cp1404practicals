MIN = 3


def main():

    password = get_password()
    while len(password) < MIN:
        print("Password wrong")
        password = get_password()
    for i in range(len(password)):
        print_stars()
    print()


def get_password():
    password = input("> ")
    return password


def print_stars():
    print("*", end='')


main()
