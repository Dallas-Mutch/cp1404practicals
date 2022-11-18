from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            choose_taxis(taxis)
            choose = int(input("Choose your taxi: "))
            try:
                current_taxi = taxis[choose]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distant_driven = float(input("Drive how far? "))
                current_taxi.drive(distant_driven)
                trip_amount = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_amount:.2f}")
                total_bill += trip_amount
            else:
                print("You need to choose a taxi before driving")
        else:
            print("Invalid input")
        print(f"Bill to date: {total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").upper()

    print(f"Bill to date: {total_bill}")
    print("Taxis are now:")
    choose_taxis(taxis)


def choose_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)

# def taxi_drive():



if __name__ == '__main__':
    main()
