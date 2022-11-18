from prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Car", 100, 90)
    other_car = UnreliableCar("Lost car", 100, 40)

    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{my_car.name:12} drove {my_car.drive(i):2}km")
        print(f"{other_car.name:12} drove {other_car.drive(i):2}km")
    print(my_car)
    print(other_car)


main()
