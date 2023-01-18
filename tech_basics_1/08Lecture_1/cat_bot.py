from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from telegram import *


YOUR_TOKEN = ""
random_cat_image = "Click here for random cat image!"


def get_cat_image():
    contents = requests.get("https://cataas.com//cat")
    cat_image = contents.content

    return cat_image


def start(update, context):
    button = [[KeyboardButton("Click here for random cat image!")]]
    reply_kb_markup = ReplyKeyboardMarkup(button)
    message = "Hello! Welcome to my cat bot :)"
    context.bot.sendMessage(chat_id = update.message.chat_id, text=message, reply_markup=reply_kb_markup)


def message_handler(update, context):
    if random_cat_image in update.message.text:
        image = get_cat_image()

    if image:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)

    buttons = [[InlineKeyboardButton("👍", callback_data="like")], [InlineKeyboardButton("👎", callback_data="dislike")]]
    message = "Did you like the image?"
    reply_inline_markup = InlineKeyboardMarkup(buttons)
    context.bot.sendMessage(chat_id = update.message.chat_id, text=message, reply_markup=reply_inline_markup)


def main():
    """Runs the program"""
    print("The bot is running in telegram")

    updater = Updater(YOUR_TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

main()
