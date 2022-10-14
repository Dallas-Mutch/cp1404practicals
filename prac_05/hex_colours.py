NAME_TO_COLOUR = {"Absolute zero": "#0048ba", "Amber": "#ffbf00",
                  "Cordovan": "#893f45", "CornflowerBlu": "#6495ed",
                  "DarkKhaki": "#bdb76b", "Denim": "#1560bd",
                  "DimGray": "#696969", "Fawn": "#e5aa70",
                  "Feldgrau	": "#4d5d53", "Emerald": "#50c878"}
print(NAME_TO_COLOUR)

colour_code = input("What colour do you want: ").title()
while colour_code != "":
    if colour_code in NAME_TO_COLOUR:
        print(f"{NAME_TO_COLOUR[colour_code]}")
    else:
        print("Invalid colour code")
    colour_code = input("What colour do you want: ").title()
