import random
import string
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print(" Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print(" Please enter a positive number.")
            return

        password = generate_password(length)
        print(f"Your generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()
