import string
import random

# reference: https://geekflare.com/password-generator-python-code/

# characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")


# ask the user the number of character types for the password
alphabets_count = int(input("Enter alphabets count in password: "))
digits_count = int(input("Enter digits count in password: "))
special_characters_count = int(input("Enter special characters count in password: "))

# you could shuffle the characters before creating password
# random.shuffle(characters)

characters_count = alphabets_count + digits_count + special_characters_count

print(f"The password contains {characters_count} characters")

# TODO: Check if that is OK with the user

# picking random characters from the list
password = [] # create a blank list

# picking random alphabets
for i in range(alphabets_count):
	password.append(random.choice(alphabets))

# picking random digits
for i in range(digits_count):
	password.append(random.choice(digits))

# picking random alphabets
for i in range(special_characters_count):
	password.append(random.choice(special_characters))

# shuffling the resultant password
random.shuffle(password)

# converting the list to string
# printing the list
password_generated = "".join(password)
print(f"The generated password with {alphabets_count} alphabets, {digits_count} digits, {special_characters_count} special characters is:", password_generated)
