import string
import random

# reference: https://geekflare.com/password-generator-python-code/

# ask the user the length of password
length = int(input("Enter password length: "))

# create a variable that will contain the pool of characters
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password_generator(characters, length):

    random.shuffle(characters)
    password = characters[0:length]

    password_generated = "".join(password)

    return password_generated


final_password = password_generator(characters, length)
print(f"The password generated is: {final_password}")