# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

MENU = """Enter name: 
(H)ello
(G)oodbye
(Q)uit
        """
print(MENU)
menu_choice = input(">>>").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello")
    elif menu_choice == "G":
        print("Goodbye")
    else:
        print("Invalid response")
    print(MENU)
    menu_choice = input(">>>").upper()
print("Finished")
