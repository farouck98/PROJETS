import string
from random import randint
from random import sample
from random import choice
from random import shuffle


def password_generation():
    length_password = randint(10, 64)

    lowercase_letters = choice(string.ascii_lowercase)
    uppercase_letters = choice(string.ascii_uppercase)
    digits = string.digits
    special_character = choice('@!=&*^!')

    all_characters = lowercase_letters + uppercase_letters + digits + special_character

    password = choice(lowercase_letters) + \
                choice(uppercase_letters) + \
                choice(digits)  + \
                choice(special_character)

    password += "".join(sample(all_characters, length_password - 4))

    list_password = list(password)
    shuffle(list_password)
    password = "".join(password)

    return password

def main():
    print(password_generation())

if __name__ == "__main__":
    main()