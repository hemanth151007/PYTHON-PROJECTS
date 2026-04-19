import re

def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("At least 8 characters required")

    if not re.search(r'[A-Z]', password):
        errors.append("Missing uppercase letter")

    if not re.search(r'\d', password):
        errors.append("Missing digit")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Missing special character")

    return errors


def main():
    while True:
        password = input("Enter password (or 'exit'): ")

        if password.lower() == "exit":
            print("Exiting...")
            break

        errors = check_password(password)

        if not errors:
            print("Strong password")
        else:
            print("Weak password:")
            for e in errors:
                print("-", e)


if __name__ == "__main__":
    main()
