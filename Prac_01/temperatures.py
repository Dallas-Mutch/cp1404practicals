"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius_p1 = float(input("Celsius: "))
        fahrenheit_p1 = celsius_p1 * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit_p1))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit_p1 = float(input("Fahrenheit: "))
        celsius_p1 = 5 / 9 * (fahrenheit_p1 - 32)
        print("Result: {:.2f} C".format(celsius_p1))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")