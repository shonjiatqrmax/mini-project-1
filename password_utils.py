import random
import string

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