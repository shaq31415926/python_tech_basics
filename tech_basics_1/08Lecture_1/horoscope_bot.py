# import libraries
import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

YOUR_TOKEN = "2021611058:AAFJkhuzdFOw5JYCZ26pvjATe2sKxD_fG6o"


# Processing commands
def start(update, context):
    """When the user enters start the following message will appear"""
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Hello, What is your horoscope??')

def get_horoscopes(sign):
    """Definition to fetch horoscope from url"""

    url = "https://ohmanda.com/api/horoscope/"

    r = requests.get(url = url + sign) # make request to horoscope_url
    data = r.json() # format the request into a dictionary

    return data["horoscope"]


def bot_response(update, context):
    """When the user types a message the bot will give the following response"""
    star_sign = update.message.text
    horoscope = get_horoscopes(star_sign)
    response = 'Your horoscope is... ' + horoscope
    context.bot.sendMessage(chat_id=update.message.chat_id, text=response)


def main():
    """Run the Program
    """
    # Create the Updater and pass it your bot's token.
    updater = Updater(YOUR_TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Add handlers to the dispatch
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, bot_response))
    # Getting Started for Updates
    updater.start_polling()
    # Stop the bot if Ctrl + C was pressed
    updater.idle()


if __name__ == '__main__':
    os.system("clear")
    main()
