# numbers = []
# for i in range(5):
#     number = int(input("Number: "))
#     numbers.append(number)
#
# print("The first number is ", numbers[0])
# print("The last number is ", numbers[-1])
# print("The smallest number is ", min(numbers))
# print("The first number is ", max(numbers))
# print("The first number is ", sum(numbers) / len(numbers))


# 2.
usernames = ['jimbo', 'giltson98', 'derekf',
             'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
user = input("Username: ")
if user in usernames:
    print("Access granted")
else:
    print("Access denied")