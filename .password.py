import random
import string

def generate_password():
    length = int(input("Enter the desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    save_to_file = input("Save passwords to a file? (y/n): ").lower() == 'y'

    for _ in range(num_passwords):
        password = generate_password()
        print("Generated Password:", password)

        if save_to_file:
            save_password_to_file(password)

if _name_ == "_main_":
    main()