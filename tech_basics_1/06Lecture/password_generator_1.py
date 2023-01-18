import string
import random

# reference: https://geekflare.com/password-generator-python-code/

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
# you also create a list with characters of your choices
# characters = ['a', 'x', 'z', '%', '']
# shuffle the characters:
random.shuffle(characters)
## ask the user the length of password
length = int(input("Enter password length: "))

## picking random characters from the list

# option 1: subset the list
password = characters[0:length]

# option 2: user for loops to subset the list
#password = [] # create a blank list
#for i in range(length):
#	password.append(random.choice(characters)) # append a random choice of charaters

random.shuffle(password)

# print the password before continuing
# print(password)
## shuffling the resultant password

## converting the list to string
## printing the list
password_generated = "".join(password)
print(f"The generated password of {length} characters is: {password_generated}")
