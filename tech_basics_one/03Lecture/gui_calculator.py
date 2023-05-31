# import the library
import tkinter as tk
from tkinter import ttk

# reference: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

# create a graphic user interface windows
# m = tk.Tk()

# change the name of the window to a name of your choice
m = tk.Tk(className='My Calc')

# set the background colour of GUI window
m.configure(background='black')

# set the configuration of GUI window
m.geometry("410x180")

# let's start by creating the text entry box for showing the expression
# expression_field = tk.Entry(m)

# grid method is used for placing the widgets at respective positions in table like structure .
# expression_field.grid(columnspan=4, ipadx=70)

# we need to add an equation field to the expression field
# for now we will store everything as a variable
# create a variable called equation and pass this in the expression field
equation = tk.StringVar()
expression_field = tk.Entry(m, textvariable=equation)
expression_field.grid(columnspan=4,  ipadx=110)


# create a Buttons and place at a particular location inside the root window .
# when user press the button, the command or function affiliated to that button is executed .

button1 = tk.Button(m,
                    text=' 1 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(1),
                    height=1,
                    width=7)
button1.grid(row=2, column=0)

# the button right now will not do anything - you should see an error saying that press is not defined
# two things we need to do to get the

# step 1, create a variable called expression which will store the what we input in the calculator
expression = ""

# step 2, create a definition that will store the values as we press the numbers and operators
def press(value):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(value)

    # update the expression by using set method
    equation.set(expression)

# to get the colour working
ttk.Style().configure('green/black.TButton', foreground='green', background='black')

button1 = tk.Button(m,
                    text=' 1 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(1),
                    height=1,
                    width=7)
button1.grid(row=2, column=0)


# if everything is working correctly, you see that the number is appearing in the expression field

# let's create a few more buttons and operators
button2 = tk.Button(m,
                    text=' 2 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(2),
                    height=1,
                    width=7)
button2.grid(row=2, column=1)

button3 = tk.Button(m,
                    text=' 3 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(3),
                    height=1,
                    width=7)
button3.grid(row=2, column=2)

button4 = tk.Button(m,
                    text=' 4 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(4),
                    height=1,
                    width=7)
button4.grid(row=3, column=0)

button5 = tk.Button(m,
                    text=' 5 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(5),
                    height=1,
                    width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(m,
                    text=' 6 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(6),
                    height=1,
                    width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(m,
                    text=' 7 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(7),
                    height=1,
                    width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(m,
                    text=' 8 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(8),
                    height=1,
                    width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(m,
                    text=' 9 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(9),
                    height=1,
                    width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(m,
                    text=' 0 ',
                    fg='black',
                    bg='red',
                    command=lambda: press(0),
                    height=1,
                    width=7)
button0.grid(row=5, column=0)

# let's create some operators

plus = tk.Button(m,
                 text=' + ',
                 fg='black',
                 bg='red',
                 command=lambda: press("+"),
                 height=1,
                 width=7)
plus.grid(row=2, column=3)

minus = tk.Button(m,
                  text=' - ',
                  fg='black',
                  bg='red',
                  command=lambda: press("-"),
                  height=1,
                  width=7)
minus.grid(row=3, column=3)

multiply = tk.Button(m,
                     text=' * ',
                     fg='black',
                     bg='red',
                     command=lambda: press("*"),
                     height=1,
                     width=7)
multiply.grid(row=4, column=3)

divide = tk.Button(m,
                   text=' / ',
                   fg='black',
                   bg='red',
                   command=lambda: press("/"),
                   height=1,
                   width=7)
divide.grid(row=5, column=3)

# we can also create a decimal point
decimal= tk.Button(m,
                   text='.',
                   fg='black',
                   bg='red',
                   command=lambda: press('.'),
                   height=1,
                   width=7)
decimal.grid(row=6, column=0)


# to get the colour working
ttk.Style().configure('green/black.TButton', foreground='green', background='black')

button1 = ttk.Button(m,
                    text=' 1 ',
                    style='green/black.TButton',
                    command=lambda: press(1))
button1.grid(row=2, column=0)


# let's create a equal button
def press_equal():
    global expression

    # eval function evaluate the expression and str function convert the result into string
    total = str(eval(expression))

    equation.set(total)


equal = tk.Button(m,
                  text=' = ',
                  fg='black',
                  bg='red',
                  command=press_equal,
                  height=1,
                  width=7)
equal.grid(row=5, column=2)

# let's create a clear button
# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

clear = tk.Button(m,
                  text='Clear',
                  fg='black',
                  bg='red',
                  command=clear,
                  height=1,
                  width=7)
clear.grid(row=5, column=1)

# you might have to execute this code to see the window pop up
m.mainloop()