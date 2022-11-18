from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Testing flagfall and fanciness for taxis"""
    other_car = SilverServiceTaxi("Ferrari", 100, 2)
    other_car.drive(18)

    print(other_car)
    print(f"Fare costs: ${other_car.get_fare()}")


if __name__ == '__main__':
    main()