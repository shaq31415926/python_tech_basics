# import libraries
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# define Your token
YOUR_TOKEN = ""

def start(update, context):
    """When the user enters start the following message will appear"""
    start_message = "Hello! How are you?"
    context.bot.sendMessage(chat_id = update.message.chat_id, text = start_message)

def bot_response(update, context):
    """When the user types a message the bot responds with the following"""
    response = "Got your message: " + update.message.text
    context.bot.sendMessage(chat_id = update.message.chat_id, text = response)

def main():
    print("Code is running in telegram bot")
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, bot_response))

    updater.start_polling()
    updater.idle()

# call our definition
main()
