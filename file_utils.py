import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "password_history.txt")

def save_password(password):
    with open(FILE_NAME,"a")as file:
        file.write(password+"\n")

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