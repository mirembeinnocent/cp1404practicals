
def main():
    password = get_password()
    print_asterisks(password)


def get_password(min_length=8):
    while True:
        password = input("Enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long.")
        else:
            return password


def print_asterisks(password):
    print("*" * len(password))


main()
