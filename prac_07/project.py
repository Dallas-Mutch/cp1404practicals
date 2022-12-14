"""CP1404 Programming II
    Time estimate: 2 days
    Time completed: 4 days
"""
import datetime


class Project:
    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t" \
               f"{self.completion_percentage}%"

    def __str__(self):
        return f"{self.name}, Start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: {self.cost_estimate}, completion: " \
               f"{self.completion_percentage}%"

    def is_completed(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority


def run_tests():
    t1 = Project("Mow lawn", datetime.datetime.strptime("12/1/2012", "%d/%m/%Y"), 3, 3.0, 0)
    print(t1)


if __name__ == '__main__':
    run_tests()
