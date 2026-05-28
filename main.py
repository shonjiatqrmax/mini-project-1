import random
import string
import os

print("test")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "password_history.txt")

def save_password(password):
    with open(FILE_NAME,"a")as file:
        file.write(password+"\n")

def get_characters(option):
    if option == "1":
        return string.ascii_letters
    elif option == "2":
        return string.ascii_letters + string.digits
    elif option == "3":
        return string.ascii_letters + string.digits + string.punctuation
    else:
        return string.ascii_letters


def generate_password(length, characters):
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

def view_history():
    try:
        with open(FILE_NAME, "r") as file:
            lines=file.readlines()

            if len(lines)==0:
                print("No saved passwords.")

            else:
                print("\n---Password History---")
                for i, line in enumerate(lines):
                    print(f"{i+1}.{line.strip()}")

    except FileNotFoundError:
        print("No saved passowrds yet.")




while True:
    print("\n===== PASSWORD GENERATOR =====")
    print("1. Generate password")
    print("2. View saved passwords")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        print("\nPassword type:")
        print("1. Letters only")
        print("2. Letters + numbers")
        print("3. Letters + numbers + symbols")

        option = input("Choose option: ")
        length = int(input("Enter password length: "))

        characters = get_characters(option)

        while True:
                password = generate_password(length, characters)
                print("Generated password:", password)
                save = input("Save this password?(y/n): ").lower()

                if save=="y":
                    save_password(password)
                    print("Password saved.")

                again = input("Generate another password with same settings? (y/n): ").lower()

                if again != "y":
                    break

    elif choice == "2":
        view_history()

    elif choice=="3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")