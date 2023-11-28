import os
from datetime import date

os.system("clear")

# ask user for their date of birth
user_dob = input("What is your date of birth? Enter in format YYYY-MM-DD:")
# converting the string dob to a datetime
year, month, day = user_dob.split("-")
year = int(year)
month = int(month)
day = int(day)


def age_calculator(year, month, day):
    """This function calculates the age based on the users year, month and day of their dob"""
    # convert the dob into a date field
    user_dob = date(year, month, day)

    # get today's date
    current_date = date.today()

    # calculate the age
    age = int((current_date - user_dob).days / 365.25)

    return age


def horoscope_calculator(month, day):
    """This function calculates the horoscope based on the users month and day of their dob"""

    if (month == 1 and day < 23) or (month == 12 and day >= 23):
        user_sign = "capricorn"
    elif (month == 2 and day < 23) or (month == 1 and day >= 23):
        user_sign = "aquarius"
    elif (month == 3 and day < 23) or (month == 2 and day >= 23):
        user_sign = "pisces"
    elif (month == 4 and day < 23) or (month == 3 and day >= 23):
        user_sign = "aries"
    elif (month == 5 and day < 23) or (month == 4 and day >= 23):
        user_sign = "taurus"
    elif (month == 6 and day < 23) or (month == 5 and day >= 23):
        user_sign = "gemini"
    elif (month == 7 and day < 23) or (month == 6 and day >= 23):
        user_sign = "cancer"
    elif (month == 8 and day < 23) or (month == 7 and day >= 23):
        user_sign = "leo"
    elif (month == 9 and day < 23) or (month == 8 and day >= 23):
        user_sign = "virgo"
    elif (month == 10 and day < 23) or (month == 9 and day >= 23):
        user_sign = "libra"
    elif (month == 11 and day < 23) or (month == 10 and day >= 23):
        user_sign = "scorpio"
    elif (month == 12 and day < 23) or (month == 11 and day >= 23):
        user_sign = "sagitarius"
    else:
        user_sign = "unknown"

    return user_sign


user_age = age_calculator(year, month, day)
user_sign = horoscope_calculator(month, day)
print(f"Your age is {user_age} and your horoscope is {user_sign.capitalize()}")
