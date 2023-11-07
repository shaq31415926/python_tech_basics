# ask the user for a word
text = input("Please enter a word:")


def length_of_word(text):
    """This function will count the length of the word"""

    word_length = len(text)

    return word_length


def reverse_string(text):
    """This function will do the following:
    - Count the length of the word
    - If the length is a multiple of four then it will print the reverse of the word, otherwise it will print the world"""

    length = length_of_word(text)
    print(f"The length is {length}")

    if length % 4 == 0:
        print(text[::-1])
    else:
        print(text)


reverse_string(text)
