import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# create the gui window
root = tk.Tk()

# title
root.title("Age Calculator 🤓")

# configure the size
screen_height = 400
screen_width = 800
root.minsize(width=screen_width, height=screen_height)


# place an image on the first screen
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

# place an image on the first page
add_image(root, "images/age_calculator.png", screen_width, screen_height)

# create an empty age label which will be updated every time the user calculates their age
age_label = tk.Label(root,
                     font=('Comic Sans MS', 24, 'bold'),
                     bg="white",
                     fg="black"
                     )
age_label.place(x=screen_width/2-70, y=screen_height / 1.5 + 50)


def calculate_age():
    # get todays date
    current_date = date.today()

    # get the users dob
    dob = cal.get_date()

    # if the year of dob is greater than existing year, subtract 100
    if dob.year > current_date.year:
        dob = dob - relativedelta(years=100)

    age = int((current_date - dob).days / 365.25)

    age_label.configure(text=f"Your age is {age}")


def calculate_age_page():
    global cal

    # destroy everything we created so far
    f1.destroy()
    entry_button.destroy()

    # change the background colour
    root.configure(background="white")

    # creating a label to ask the user for their date of birth
    dob_label = tk.Label(root,
                         text="SELECT YOUR DATE OF BIRTH =)",
                         font=('Comic Sans MS', 44, 'bold'),
                         fg="black",
                         bg="white"
                         )
    #dob_label.pack(anchor="center")
    dob_label.place(x=30, y=screen_height/4)

    style = tk.ttk.Style()
    style.configure('my.DateEntry',
                    foreground='dark blue',
                    arrowcolor='white')

    # creating a calendar entry point
    cal = DateEntry(root,
                    font="Arial 20",
                    selectmode="day",
                    style='my.DateEntry'
                    )
    #cal.pack(anchor="center", padx=10, pady=10)
    cal.place(x=screen_width/2-65, y=screen_height / 2)

    # button to calculate the age
    calc_age_button = tk.Button(root,
                              text="CALCULATE THE AGE",
                              font=('Comic Sans MS', 24, 'bold'),
                              command=calculate_age
                              )
    #calc_age_button.pack(anchor="center", padx=10, pady=10)
    calc_age_button.place(x=screen_width/2-130, y=screen_height / 1.5)



# create an entry button which will enter the next page
entry_button = tk.Button(root,
                        text="CLICK HERE TO CALCULATE YOUR AGE :)",
                        bg = "blue",
                        font="Arial 20 bold",
                        command=calculate_age_page)
#entry_button.place(x=screen_width/2, y=300)
entry_button.pack(anchor="center")


# launch the gui window
root.mainloop()