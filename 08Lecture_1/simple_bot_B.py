# import libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# create a token variable
YOUR_TOKEN = "2021611058:AAFJkhuzdFOw5JYCZ26pvjATe2sKxD_fG6o"

def start(update, context):
    """When the user starts the following message will send"""
    message = "Hello! How are you?"
    context.bot.sendMessage(chat_id = update.message.chat_id, text=message)

def bot_response(update, context):
    """When the user types a message the bot will give the following response"""
    response = "Got your message: " + update.message.text
    context.bot.sendMessage(chat_id = update.message.chat_id, text=response)

def main():
    """Runs the program - a simple bot that echoes what the user is saying"""
    print("The bot is running in telegram")

    updater = Updater(YOUR_TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, bot_response))

    updater.start_polling()
    updater.idle()

main()
