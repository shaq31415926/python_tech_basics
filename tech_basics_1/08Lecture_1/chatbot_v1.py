import random
import os
# import emoji

os.system("clear") # code to clear the screen. use cls if you have windows.

# simple bot to ask user for name
print("BOT: What is your name")
user_name = input()
emoji = ("\U0001f600")
# print(emoji.emojize(":winking_face_with_tongue:"))
# print(emoji.emojize(":zipper-mouth_face:"))
print(f"BOT: Nice to meet you {user_name} {emoji}")

# create a list with some responses
bot_name = "Bob"

responses = [f"They call me {bot_name}!",
            f"I usually go by {bot_name}.",
            f"My name is {bot_name} :)"]

# bot randomly chooses a respose
print("BOT:", random.choice(responses))

# create some random questions the bot will ask
# right now the bot will just return the response

while True:
    question = ["How are you?",
                "What is the weather like?"]

    print("BOT:", random.choice(question))
    user_answer = input()

    if user_answer in ["bye", "stop", "exit"]:
        break
    else:
        print(f"BOT: Your answer was {user_answer}")
