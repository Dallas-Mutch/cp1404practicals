CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise guitars"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns string for data in init"""
        return f"Guitar={self.name}({self.year}) : {self.cost}"

    def get_age(self):
        """Get age of the guitar in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
