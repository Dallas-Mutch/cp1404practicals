from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    # reliability = float(random.randint(0, 100))

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove
