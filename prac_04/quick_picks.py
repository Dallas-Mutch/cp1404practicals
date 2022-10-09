import random
MIN_NUMBER = 1
MAX_NUMBER = 45
ROW_OF_NUMBERS = 6


def main():

    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number, cannot be 0")
        number_of_quick_picks = int(input("How many quick picks? "))

    for column in range(number_of_quick_picks):
        quick_pick = []
        for row in range(ROW_OF_NUMBERS):
            numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
            while numbers in quick_pick:
                numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(numbers)
        quick_pick.sort()
        print(" ".join(f"{numbers:2}" for numbers in quick_pick))


main()
