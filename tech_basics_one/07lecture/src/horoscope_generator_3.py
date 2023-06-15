import requests

while True:
    print("-" * 50)
    user_sign = input("What is your star sign?:")
    user_sign = user_sign.lower()  # lowercase the input
    print("-" * 50)

    horoscope_url = "https://ohmanda.com/api/horoscope/"


    def get_horoscope(user_sign, url):
        """Method that sends a request to an API"""
        r = requests.get(url=url + user_sign)
        data = r.json()  # to turn the request into a dictionary
        return data["horoscope"]


    try:
        horoscope = get_horoscope(user_sign, horoscope_url)
        print("-" * 50, "\n", horoscope, "\n", "-" * 50)
        break
    except:
        print("Please double check the star sign you entered")
