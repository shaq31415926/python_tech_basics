import datetime
# Reference: https://codedec.com/tutorials/write-a-python-program-to-validate-the-date-of-birth/

while True:
    print("-"*50)
    user_dob = input("What is your birthday? Please enter in the following format YYYY-MM-DD:")

    # user_month, user_day = map(int, user_dob.split('-'))
    user_year, user_month, user_day = user_dob.split('-')
    user_year = int(user_year)
    user_month = int(user_month)
    user_day = int(user_day)

    try:
        datetime.datetime(int(user_year),int(user_month),int(user_day))
        print("-"*50)

        # use if-else statement to identify star_sign
        if (user_month == 1 and user_day < 22) or (user_month == 12 and user_day >= 22):
            user_sign = "Capricorn"
        elif (user_month == 2 and user_day < 22) or (user_month == 1 and user_day >= 22):
            user_sign = "Aquarius"
        elif (user_month == 3 and user_day < 22) or (user_month == 2 and user_day >= 22):
            user_sign = "Pisces"
        elif (user_month == 4 and user_day < 22) or (user_month == 3 and user_day >= 22):
            user_sign = "Aries"
        elif (user_month == 5 and user_day < 22) or (user_month == 4 and user_day >= 22):
            user_sign = "Taurus"
        elif (user_month == 6 and user_day < 22) or (user_month == 5 and user_day >= 22):
            user_sign = "Gemini"
        elif (user_month == 7 and user_day < 22) or (user_month == 6 and user_day >= 22):
            user_sign = "Cancer"
        elif (user_month == 8 and user_day < 22) or (user_month == 7 and user_day >= 22):
            user_sign = "Leo"
        elif (user_month == 9 and user_day < 22) or (user_month == 8 and user_day >= 22):
            user_sign = "Virgo"
        elif (user_month == 10 and user_day < 22) or (user_month == 9 and user_day >= 22):
            user_sign = "Libra"
        elif (user_month == 11 and user_day < 22) or (user_month == 10 and user_day >= 22):
            user_sign = "Scorpio"
        elif (user_month == 12 and user_day < 22) or (user_month == 11 and user_day >= 22):
            user_sign = "Sagittarius"

        print("Your Astrological sign is :", user_sign)
        # lower case the user_sign or update your dictionary
        user_sign = user_sign.lower()

        # create a dict that contains stair signs and horoscopes
        horoscopes_dict = {"scorpio": "If this whole Mercury-retrograde business has left you longing for a little alone time, you may be grateful for Saturday’s cosmic news report! Serious Saturn shifts into reverse in Aquarius and your fourth house of domesticity, which can give you the wherewithal to RSVP “no thank you” to invitations that leave you underwhelmed. As the zodiac’s most private sign, you need to keep a little wall around your home and personal life, and a good way to accomplish that is by making Chateau Scorpio your safe and isolated sanctuary. But is it comfortable? Does your physical space accommodate your homey needs? With Saturn in reverse, you may be RE-considering a whole list of things you want to RE-do, like rearrange furniture, change some room layouts or maybe just don the painter’s coveralls and start rolling! But there’s no winging it with Saturn in the director’s chair. You need a well-thought-out game plan, and the good news is, you’ve got five months to create it. The clock starts…now!",
                           "pisces": "....",
                           "taurus": "...",
                           "libra": ".....",
                           "aries": "....",
                           "sagitarius": "..",
                           "capricorn": "....",
                           "virgo": "...",
                           "leo": ".....",
                           "cancer": "....",
                           "gemini": "..",
                           "aquarius": ".."
                        }

        # if horoscope is not a registered horoscope then error
        known_sign = list(horoscopes_dict.keys())

        if user_sign in known_sign:
            print(horoscopes_dict[user_sign])
            break # we no longer loop through the code if the sign is found
        else:
            print("We do not recognise your horoscope. Please check the spellings")

        break

    except ValueError:
        print("Please Enter Correct Date of Birth.")
