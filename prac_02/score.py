"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    if score_range(score):
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def score_range(score):
    return score < 0 or score > 100


score_random = random.randrange(0, 100)
print(f"Your random score is: {score_random}")

main()
