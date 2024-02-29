
def main():
    score = get_valid_score()
    while True:
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_score_status(score)}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def determine_score_status(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * int(score))


def get_valid_score():

    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
            return score
        except ValueError as e:
            print(e)


main()
