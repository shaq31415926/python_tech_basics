import requests

while True:
    print("-"*50)
    user_sign = input("What is your star sign?:")
    user_sign  = user_sign.lower() # lowercase the input
    user_sign = user_sign.strip() # removes white spaces
    print("-"*50)

    horoscope_url = "https://ohmanda.com/api/horoscope/"

    def get_horoscopes(url, sign):
        """Definition to fetch horoscope from url"""

        r = requests.get(url = url + sign) # make request to horoscope_url
        data = r.json() # format the request into a dictionary

        return data["horoscope"]

    try:
        horoscope = get_horoscopes(horoscope_url, user_sign)
        print(horoscope)
        break
    except:
        print("Star sign not found")
