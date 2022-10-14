"""
CP1404/CP5632 Practical
State names in a dictionary
File reformatted and neatly aligned
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Loop that prints the names and states neatly:
for i in CODE_TO_NAME.items():
    print(f"{i[0]:3} is\t {i[1]}")



