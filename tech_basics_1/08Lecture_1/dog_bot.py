from telegram import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

YOUR_TOKEN = ""

def get_dog_image():
    """Access the API and get the image URL"""
    contents = requests.get('https://random.dog/woof.json').json()
    dog_image = contents['url']
    return dog_image


def start(update, context):
    """The command the bot carries out when starting the bot"""
    print("all working!")
    dog_image = get_dog_image()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_image)


def main():
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
