# number_of_items = int(input("Number of items: "))
#
# total = 0
# for i in range(number_of_items):
#     item_prices = float(input("Price of item: "))
#     total+= item_prices
# if total > 100:
#     discount = total / 1.1
#     print(f"Total item price is ${discount:.2f}")
# else:
#     print("Total item price is $", total)

# while number_of_items >= 0:
#     item_prices = float(input("Price of item: "))
#     total += item_prices
# if total >= 100:
#     discount = total / 1.1
#     print(f"Total item price is ${discount:.2f}")
# elif total <= 0:
#     print("Total item price is $", total)
# print("Invalid")

# Error checking
# number_of_items = int(input("Number of items: "))
# while number_of_items < 0:
#     print("Invalid!")
#     number_of_items = int(input("Number of items: "))
# print("number of items is...", number_of_items)

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid!")
    number_of_items = int(input("Number of items: ")                      )
for i in range(number_of_items):
    item_prices = float(input("Price of item: "))
    total += item_prices
    if total > 100:
        total *= 0.9  # 10% discount
print(f"Total price for {number_of_items} is ${total:.2f}")