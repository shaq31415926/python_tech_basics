import tkinter as tk

# This code was inspired by: https://thecleverprogrammer.com/2021/01/24/screen-pet-with-python/#google_vignette


def show_happy(c):

    show_neutral(c)

    c.itemconfigure(cheek_left, state=tk.NORMAL)
    c.itemconfigure(cheek_right, state=tk.NORMAL)
    c.itemconfigure(mouth_happy, state=tk.NORMAL)
    c.itemconfigure(mouth_normal, state=tk.HIDDEN)



def show_neutral(c):
    c.itemconfigure(cheek_left, state=tk.HIDDEN)
    c.itemconfigure(cheek_right, state=tk.HIDDEN)
    c.itemconfigure(mouth_happy, state=tk.HIDDEN)
    c.itemconfigure(mouth_normal, state=tk.NORMAL)
    c.itemconfigure(mouth_sad, state=tk.HIDDEN)
    c.itemconfigure(tongue_tip, state=tk.HIDDEN)
    c.itemconfigure(tongue_main, state=tk.HIDDEN)


def show_sad(c):
    show_neutral(c)

    c.itemconfigure(mouth_happy, state=tk.HIDDEN)
    c.itemconfigure(mouth_normal, state=tk.HIDDEN)
    c.itemconfigure(mouth_sad, state=tk.NORMAL)


def toggle_tongue(c):
    c.itemconfigure(tongue_tip, state=tk.NORMAL)
    c.itemconfigure(tongue_main, state=tk.NORMAL)


def toggle_pupils(c):
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False


def show_cheeky(c, root):
    show_neutral(c)

    toggle_tongue(c)
    toggle_pupils(c)
    # reset the pupils after one sec
    root.after(1000, lambda:toggle_pupils(c))


def toggle_eyes(c):
    current_color = c.itemcget(eye_left, 'fill')
    if current_color == 'white':
        new_color = c.body_color
    else:
        new_color = 'white'
    current_state = c.itemcget(pupil_left, 'state')
    if current_state == tk.HIDDEN:
        new_state = tk.NORMAL
    else:
        new_state = tk.HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink(root, c):
    toggle_eyes(c)
    root.after(250, lambda:toggle_eyes(c))
    root.after(2500, lambda:blink(root, c))


def online_pet(root):
    global cheek_left, cheek_right, mouth_happy, mouth_normal, mouth_sad, tongue_tip, tongue_main, pupil_left, pupil_right, eye_left, eye_right

    c = tk.Canvas(root, width=400, height=400)
    c.configure(bg='dark blue', highlightthickness=0)
    c.body_color = 'SkyBlue1'

    c.eyes_crossed = False

    # this creates the body of the cat - storing this as variables to do further manipulation in the future
    body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
    ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
    ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
    foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
    foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

    # these are attributes of the pet we will manipulate
    eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
    pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
    eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
    pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

    mouth_normal = c.create_line(170, 250, 200, 250, 230, 250, smooth=1, width=2, state=tk.NORMAL)
    mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=tk.HIDDEN)
    mouth_sad = c.create_line(170, 250, 200, 202, 230, 250, smooth=1, width=2, state=tk.HIDDEN)
    tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=tk.HIDDEN)
    tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=tk.HIDDEN)

    cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=tk.HIDDEN)
    cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=tk.HIDDEN)

    c.pack()

    # this will create an online pet that blinks continuously
    blink(root, c)

    # place buttons so the user can change the mood based on selection
    happy = tk.Button(root,
                      text="happy",
                      command=lambda:show_happy(c))
    happy.place(x=2, y=50)

    reset = tk.Button(root,
                      text="neutral",
                      command=lambda:show_neutral(c))
    reset.place(x=2, y=90)

    sad = tk.Button(root,
                      text="sad",
                      command=lambda: show_sad(c))
    sad.place(x=2, y=130)

    cheeky = tk.Button(root,
                    text="cheeky",
                    command=lambda: show_cheeky(c, root))
    cheeky.place(x=2, y=10)

