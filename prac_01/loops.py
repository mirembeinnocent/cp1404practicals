# a count in 10s from 0 to 100.

for i in range(0, 101, 10):
    print(i, end="")
print()


# b count down from 20 to 1.

for i in range(20, 0, -1):
    print(i, end="")
print()


# c print n stars. Ask the user for a number, then print that many stars (*), all on one line..

num_of_stars = int(input("Enter number of stars: "))
for _ in range(num_of_stars):
    print("*", end="")
print()


# d.

amount_of_stars = int(input("Enter number of stars: "))
for i in range(1, amount_of_stars + 1):
    print("*" * i)
