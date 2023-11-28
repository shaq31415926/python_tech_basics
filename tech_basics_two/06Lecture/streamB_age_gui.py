import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date
from dateutil.relativedelta import relativedelta

# create the gui window
root = tk.Tk()

# give it a title
root.title("Age Calculator 🤓")

# change the size of the gui
screen_height = 400
screen_width = 800
root.minsize(height=screen_height, width=screen_width)


def add_image(root, file_path, width, height):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1

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

# place a background image
add_image(root, "images/age_calculator.png", screen_width, screen_height)


def calculate_age():
    dob = cal.get_date()

    # get today's date
    current_date = date.today()

    # logic that identifies dob that have been incorrectly formatted
    if dob.year > current_date.year:
        dob = dob - relativedelta(years=100)

    # calculate the age
    age = int((current_date - dob).days / 365.25)

    # add a label to show the age
    age_label = tk.Label(root,
             text=f"Your age is {age}",
             font="Arial 20 bold")
    age_label.place(x=400, y=200)


def age_calculator_page():
    global cal

    # destroys everything you created on the first page
    f1.destroy()
    entry_button.destroy()

    # change the background colour
    root.configure(background="white")

    # add a label
    dob_label = tk.Label(root,
                         text="SELECT YOUR DATE OF BIRTH",
                         font="Arial 20 bold",
                         bg="white",
                         fg="blue"
                         )
    dob_label.pack(anchor="center")

    # add the calendar entry
    cal = DateEntry(root,
                    width=20,
                    font="Arial 20",
                    select_mode="day"
                    )
    cal.place(x=270, y=50)

    # CREATE ANOTHER BUTTON
    age_calc_button = tk.Button(root,
                        text="CLICK HERE TO CALCULATE YOUR AGE",
                        font="Arial 16",
                        bg="blue",
                        command=calculate_age)
    age_calc_button.place(x=240, y=100)






# place an entry button
entry_button = tk.Button(root,
                        text="Click here to enter the age calculator",
                        font="Arial 20 bold",
                        command=age_calculator_page
                         )
#entry_button.place(x=100, y=100)
entry_button.pack(anchor="center")

# launch my gui
root.mainloop()