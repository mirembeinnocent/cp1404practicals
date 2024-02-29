def main():
    name = input("Enter name: ")
    choice = ''

    while choice != 'Q':
        display_menu()
        choice = get_choice()

        if choice == 'H':
            print("Hello", name)
        elif choice == 'G':
            print("Goodbye", name)
        elif choice != 'Q':
            print("Invalid choice")

    print("Finished.")


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def get_choice():
    return input(">>> ").upper()


main()
