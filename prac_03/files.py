# 1.

name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# 2.

with open("name.txt", "r") as file:
    name = file.read()
    print(f"Your name is {name}")

# 3.

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()[:2]]
    total = sum(numbers)
    print("Total of first two numbers:", total)

# 4.

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]
    total = sum(numbers)
    print("Total of all numbers:", total)
