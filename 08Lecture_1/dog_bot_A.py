# import libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import *
import requests

# define Your token
YOUR_TOKEN = ".."

def get_dog_image():
    """Access the API that contains a dog image"""
    contents = requests.get("https://random.dog/woof.json").json()
    dog_image = contents["url"]

    return dog_image

def start(update, context):
    """When the user enters start the image will appear"""
    button = [[KeyboardButton("Click here for Random Dog Image")]] # create button
    reply_kb_markup = ReplyKeyboardMarkup(button, resize_keyboard = True)
    context.bot.send_message(chat_id = update.effective_chat.id,
    text = "Hi! Welcome to my Bot!", reply_markup=reply_kb_markup)
    #dog_image = get_dog_image()
    #context.bot.send_photo(chat_id = update.effective_chat.id, photo = dog_image)

random_dog_image = "Click here for Random Dog Image"

def message_handler(update, context):
    if random_dog_image in update.message.text:
        image = get_dog_image()

    if image:
        context.bot.send_photo(chat_id = update.effective_chat.id, photo = image)

    buttons = [[InlineKeyboardButton("👍", callback_data="like")], [InlineKeyboardButton("👎", callback_data="dislike")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text = "Did you like the image?")



def main():
    print("Bot is running in telegram bot")
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

# call our definition
main()
