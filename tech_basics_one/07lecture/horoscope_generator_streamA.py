import os
import requests
import time

# code to clear the screen
os.system("clear")  # cls for window users

horoscope_url = "https://ohmanda.com/api/horoscope/"


def get_horoscope(url, user_sign):
    """Method sends a request to the ohmanda api"""
    r = requests.get(url=url + user_sign)
    # this converts the request to a dictionary so we can fetch the horoscope
    horoscope = r.json()["horoscope"]
    return horoscope

# ask the user for their star sign
print("-" * 100)
user_sign = input("Hey! What is your star sign:")
user_sign = user_sign.lower()
print("-" * 100)

while True:
    try:
        horoscope = get_horoscope(horoscope_url, user_sign)
        print(f"Your horoscope for today is .....")
        time.sleep(1)
        print(horoscope)
        # print("-" * 50, "\n", horoscope, "\n", "-" * 50)
        print("BYE!! Check again tomorrow!!")
        break
    except:
        print("Error - this star sign does not exist")
        user_sign = input("PLEASE CHECK YOUR SPELLINGS!!! WHAT IS YOUR STAR SIGN:")
        user_sign = user_sign.lower()
