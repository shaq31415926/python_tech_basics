from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

YOUR_TOKEN = "2021611058:AAFJkhuzdFOw5JYCZ26pvjATe2sKxD_fG6o"
random_dog_image = "Random Dog Image"
random_cat_image = "Random Cat Image"


def start(update, context):
    """The command the bot carries out when starting the bot"""
    print("all working!")
    # url = get_url()
    # print a keyboard and a welcome message
    button = [[KeyboardButton("Random Dog Image")], [KeyboardButton("Random Cat Image")]]
    reply_kb_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Welcome to my Dog and Cat Bot!", reply_markup=reply_kb_markup)
    # print(update.effective_chat.username)
    # print(update.message.text)


def get_dog_image():
    """Access the API and get the image URL"""
    contents = requests.get('https://random.dog/woof.json').json()
    dog_image = contents['url']
    return dog_image


def get_cat_image():
    """Access the API and get the image URL"""
    contents = requests.get('https://cataas.com//cat')
    # contents = requests.get('https://cataas.com//cat/gif')
    cat_image = contents.content
    return cat_image


def message_handler(update, context):
    if random_dog_image in update.message.text:
        image = get_dog_image()

    if random_cat_image in update.message.text:
        image = get_cat_image()

    if image:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)

    # just for demonstration
    buttons = [[InlineKeyboardButton("👍", callback_data="like")],
    [InlineKeyboardButton("👎", callback_data="dislike")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text = "Did you like the image?")

def main():
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
