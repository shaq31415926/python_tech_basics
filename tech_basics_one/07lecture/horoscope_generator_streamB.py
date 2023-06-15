import requests
import os

os.system("clear")  # use cls if you have a windows

# user enters their horoscope
print("-" * 50)
user_sign = input("What is your star sign?:")
user_sign = user_sign.lower()  # lowercase the input
print("-" * 50)

# add the url
horoscope_url = "https://ohmanda.com/api/horoscope/"


def get_horoscope(url, user_sign):
    """This function gets the horoscope from the ohmada api"""
    r = requests.get(url=url + user_sign)
    # wrapping the request as a dictionary and fetching the horoscope
    horoscope = r.json()["horoscope"]

    return horoscope


while True:
    try:
        horoscope = get_horoscope(horoscope_url, user_sign)
        print("Your horoscope for today is......")
        print(horoscope)
        print("Check again tomorrow :)")
        break
    except:
        print("Error! Star sign not found")
        user_sign = input("Please enter the correct sign:").lower()
