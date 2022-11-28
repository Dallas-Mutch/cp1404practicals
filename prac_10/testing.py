"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


# 1. fix the repeat_string function above so that it passes the failing test
def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return "-".join([s] * n)


def is_long_word(word, length=5):
    # 4. Fix the failing is_long_word function
    """
        Determine if the word is as long or longer than the length passed in
        >>> is_long_word("not")
        False
        >>> is_long_word("supercalifrag")
        True
        >>> is_long_word("Python", 6)
        True
        """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    # assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # 2. write assert statements to show if Car sets the fuel correctly
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car(fuel=50)
    assert test_car.fuel == 50

def header(phrase):
    # 5. Write and test a function to format a phrase as a sentence,
    # starting with a capital and ending with a single full stop.
    # Important: start with a function header and just use pass as the body
    # then add doctests for 3 tests:
    # 'hello' -> 'Hello.'
    # 'It is an ex parrot.' -> 'It is an ex parrot.'
    # and one more you decide (one that is valid!)
    # test this and watch the tests fail
    # then write the body of the function so that the tests pass
    """
        Checking three phrases and captialize the first letter of each, and adding full stops.
        >>> header('hello')
            'Hello.'
        >>> header('It is an ex parrot.')
            'It is an ex parrot.'
        >>> header('my favourite colour is blue.')
            'My favourite colour is blue.'
        """
    sentence = phrase.capitalize()

    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

#  3. Uncomment the following line and run the doctests
doctest.testmod()


# (don't change the tests, change the function!)

