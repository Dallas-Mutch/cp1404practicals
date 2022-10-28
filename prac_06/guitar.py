class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"Guitar={self.name}({self.year}: {self.cost})"

    def get_age(self, age):
        self.year -= age
        return age

    def is_vintage(self, age):
        if self.get_age(age) > 50:
            return True
