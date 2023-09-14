import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + \
        uppercase_letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    try:
        password_length = int(input("Password Length is: "))
        if password_length <= 0:
            print("Please enter a positive integer for the password length.")
        else:
            break
    except ValueError:
        print(
            "Invalid input. Please enter a valid positive integer for the password length.")

password = generate_password(password_length)
print(f"Generated Password: {password}")