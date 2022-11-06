"""CP1404 Programming II
    Time estimate: 2 days
    Time completed:
"""
import datetime


class Project:
    def __init__(self, name, date, priority, cost, completion):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, Start: {self.date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: {self.cost}, completion: " \
               f"{self.completion}%"

    def is_completed(self):
        return self.completion == 100
