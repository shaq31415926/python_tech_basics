import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date
from dateutil.relativedelta import relativedelta
from helpers import horoscope_calculator

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Age Calculator 🤓")

# code to configure the size
width = 800
height = 400
root.minsize(width=width, height=height)


def add_image(root, file_path):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1, width, height

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()


# call our add_image function with the root variable image file path
add_image(root, file_path="../images/age_calculator.png")


def calculate_age(dob):
    # Get the current date
    current_date = date.today()

    print(dob.year, current_date.year)

    if dob.year > current_date.year:
        dob = dob - relativedelta(years=100)

    # calculate the age of the user
    age = int((current_date - dob).days / 365.2425)

    age_label = tk.Label(root,
                         text=f"Your age is {age}",
                         font="Arial 14 bold")
    age_label.place(x=370, y=190)


def calculate_horoscope(dob):
    dob = cal.get_date()

    # calculate the horoscope
    user_month = int(dob.month)
    user_day = int(dob.day)

    user_sign = horoscope_calculator(user_month, user_day)
    horoscope_label = tk.Label(root,
                               text=f"Your horoscope is {user_sign.capitalize()}",
                               font="Arial 14 bold")
    horoscope_label.place(x=330, y=220)

    # TODO: place an image of the star sign

    # TODO: add a label that gives the horoscope


def age_and_horoscope_generator():
    # kill the labels that are created once they are created

    dob = cal.get_date()

    calculate_age(dob)
    calculate_horoscope(dob)


def age_calculator_page():
    global cal

    """
    This definition creates the age calculator page
    """
    # destroy all the objects we create in our first page
    f1.destroy()
    enter_button.destroy()

    # Set the background colour of GUI window
    root.configure(background="white")

    # create three boxes to get the day, month, and year
    # Create a label - Date Of Birth
    dob_label = tk.Label(root,
                         text="Please select your date of birth",
                         bg="white",
                         fg="black",
                         font="Helvetica 34 bold ")

    # Center the label horizontally
    dob_label.pack(anchor="center")

    # creates a calendar entry box
    cal = DateEntry(root,
                    width=20,
                    font="Arial 20",
                    selectmode='day',
                    year=2023, month=11, day=27)
    cal.place(x=width / 2 - 120, y=70)

    # Button to get calculate age
    get_date_button = tk.Button(root,
                                text="Calculate age",
                                command=age_and_horoscope_generator,
                                font="Arial 16 bold")
    get_date_button.place(x=350, y=150)


# add a box on the first gui window, that will clear everything and launch a new page
enter_button = tk.Button(text="Click here to calculate your age",
                         font='lucida 20 bold',
                         command=age_calculator_page,
                         fg="blue")
# play around with the x and y coordinates to place your button
# enter_button.place(x=250, y=350)
enter_button.pack(anchor="center")

# check our this script here if you want to add a back button that goes to the first page
# https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_one/10Lecture/gui_v2.py

# code to execute the code
root.mainloop()
