from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            choose_taxis(taxis)
        elif choice == "D":
            pass
        else:
            print("Invalid input")
        print(f"Bill to date: {taxis[0]}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").upper()
    print("Bye")


def choose_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)
    choose = int(input("Choose your taxi: "))
    taxi = taxis[choose]
    print(taxi)

# def taxi_drive():



if __name__ == '__main__':
    main()
