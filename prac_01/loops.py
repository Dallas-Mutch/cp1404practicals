# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()


"""
a. count in 10s from 0 to 100
"""
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

"""
b. countdown from 20 to 1
"""

# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

"""
c. print n stars
"""
# number_of_stars = int(input("Number of stars: "))
# for number_of_stars in range(0, number_of_stars):
#     print("*", end=' ')



"""
d. print n lines increasing stars
"""

stars = int(input("Number of stars: "))
for i in range(0, stars):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()