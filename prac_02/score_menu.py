"""
"G"et a valid score (must be 0-100 inclusive)
"P"rint result (copy or import your function from score.py)
 print stars (this should print as many stars as the score)
"Q"uit
"""


def main():
    score = ""
    print("Menu:")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            score_results(score)
            print_score_star(score)
        else:
            print("Invalid option")
        print("Menu: ")
        choice = input("> ").upper()
    print("Good-Bye")


def get_valid_score():
    score = int(input("What is your score?: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("What is your score?: "))
    return score

def score_results(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def print_score_star(score):
    for i in range(score):
        print("*", end="")


main()
