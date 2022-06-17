import string
import random

# hacker 101


def password_generator(characters, length):

    password = characters[0:length]

    random.shuffle(password)

    # print the password before continuing
    # print(password)
    ## shuffling the resultant password

    ## converting the list to string
    ## printing the list
    password_generated = "".join(password)
    print(password_generated)

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
# you also create a list with characters of your choices
# characters = ['a', 'x', 'z', '%', '']
# shuffle the characters:
random.shuffle(characters)

for i in range(10000):
    for l in range(5,20):
        password_generator(characters, l)
