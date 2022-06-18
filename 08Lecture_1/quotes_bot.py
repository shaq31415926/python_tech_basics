from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time

# list of quotes

YOUR_TOKEN = "2021611058:AAFJkhuzdFOw5JYCZ26pvjATe2sKxD_fG6o"


# loop through the quotes
def start(update, context):
    quotes = [
        'First, solve the problem. Then, write the code. – John Johnson',
        'Experience is the name everyone gives to their mistakes. – Oscar Wilde',
        'Code is like humor. When you have to explain it, it’s bad. – Cory House',
        'Before software can be reusable it first has to be usable. – Ralph Johnson',
        'Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck'
    ]

    for quote in quotes:
        context.bot.sendMessage(chat_id=update.message.chat_id, text=quote)
        # sends new quotes every 20seconds
        time.sleep(10)

def main():
    """Run the Program

    Every time you enter the command /start the bot will return a random image of a dog
    """
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

main()
