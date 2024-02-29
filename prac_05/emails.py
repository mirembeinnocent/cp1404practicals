
def main():
    email_dict = {}
    while True:
        email = input("Email: ")
        if not email:
            break
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm == "n":
            name = input("Name: ").title()
        email_dict[email] = name

    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name(email):
    return email.split('@')[0].title()


main()
