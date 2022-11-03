MENU = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date
- (A)dd new project\n- (U)pdate project\n- (Q)uit"""
FILENAME = "projects.txt"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_file = open(FILENAME, "r")
            name = in_file.read()
            print(name)
            in_file.close()
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "D":
            pass
        elif choice == "D":
            pass
        elif choice == "D":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


if __name__ == '__main__':
    main()