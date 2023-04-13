import random
import string

def generate_password(length):
    # The character set to be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # The random module used to select random characters
    secure_random = random.SystemRandom()

    # The password made up of random characters
    password = ''.join(secure_random.choice(characters) for i in range(length))

    return password

# Get the password length from the user
length = int(input("Enter password length: "))

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
