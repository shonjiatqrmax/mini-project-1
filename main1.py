from password_utils import (
    get_characters,
    generate_password
)

from file_utils import (
    save_password,
    view_history
)

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