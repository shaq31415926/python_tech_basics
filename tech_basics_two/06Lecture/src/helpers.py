def horoscope_calculator(user_month, user_day):
    """
    This definition calculates the hososcope of the user based on the day and month
    """

    # use if-else statement to identify star_sign
    if (user_month == 1 and user_day < 22) or (user_month == 12 and user_day >= 22):
        user_sign = "capricorn"
    elif (user_month == 2 and user_day < 22) or (user_month == 1 and user_day >= 22):
        user_sign = "aquarius"
    elif (user_month == 3 and user_day < 22) or (user_month == 2 and user_day >= 22):
        user_sign = "pisces"
    elif (user_month == 4 and user_day < 22) or (user_month == 3 and user_day >= 22):
        user_sign = "aries"
    elif (user_month == 5 and user_day < 22) or (user_month == 4 and user_day >= 22):
        user_sign = "taurus"
    elif (user_month == 6 and user_day < 22) or (user_month == 5 and user_day >= 22):
        user_sign = "gemini"
    elif (user_month == 7 and user_day < 22) or (user_month == 6 and user_day >= 22):
        user_sign = "cancer"
    elif (user_month == 8 and user_day < 22) or (user_month == 7 and user_day >= 22):
        user_sign = "leo"
    elif (user_month == 9 and user_day < 22) or (user_month == 8 and user_day >= 22):
        user_sign = "virgo"
    elif (user_month == 10 and user_day < 22) or (user_month == 9 and user_day >= 22):
        user_sign = "libra"
    elif (user_month == 11 and user_day < 22) or (user_month == 10 and user_day >= 22):
        user_sign = "scorpio"
    elif (user_month == 12 and user_day < 22) or (user_month == 11 and user_day >= 22):
        user_sign = "sagitarius"

    return user_sign