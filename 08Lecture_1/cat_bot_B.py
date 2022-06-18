from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

YOUR_TOKEN = "..."

def get_cat_image():
    contents = requests.get("https://cataas.com//cat")
    cat_image = contents.contents

    return cat_image


def main():
    """Runs the program"""
    print("The bot is running in telegram")

    updater = Updater(YOUR_TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

main()
