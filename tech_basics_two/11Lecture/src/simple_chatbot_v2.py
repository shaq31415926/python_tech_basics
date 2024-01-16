# Reference: The code was inspired by https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/
import tkinter as tk


# create variables to format
bg_colour = "#17202A"
text_colour = "#EAECEE"
font = "Helvetica 14"
font_bold = "Helvetica 13 bold"


def send():
    # fetch the user message and store as a variable
    user_message = entry_box.get()

    # if the user enters a message
    if user_message:
        text_box.insert(tk.END, f"\nUser: {user_message}")
        #text_box.insert(tk.END, f"\nBot: {user_message}")
        text_box.insert(tk.END, "\n" + "Bot: You are 75,000th in line. Please contact XX for immediate support" )
        text_box.insert(tk.END, "\n" + "Bot has self destructed. 🎆")
        # the chatbot self destructs
        entry_box.destroy()
        send_button.destroy()

    # remove the text from the entry box
    entry_box.delete(0, tk.END)


def create_chatbot(root):
    global entry_box, send_button, text_box

    # place a welcome label
    welcome_label = tk.Label(root,
                             text="Welcome to the ChatBot",
                             bg=bg_colour,
                             fg=text_colour,
                             font=font_bold,
                             # pady=10,
                             width=30,
                             height=1)
    welcome_label.place(relx=0.5,
                        y=17,
                        anchor=tk.CENTER)  # place in center

    # create the text box
    text_box = tk.Text(root,
                       bg=bg_colour,
                       fg=text_colour,
                       font=font,
                       width=60)
    text_box.place(x=0, y=30, relwidth=1, relheight=1)  # these attributes ensure it takes up the entire screen
    # add some text that introduces the chatbot
    text_box.insert(tk.END, "Bot: Hi there, what can I do for you? Please ask your question below")

    # create a scrollbar for the textbox
    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1,
                     relx=0.974)

    # create an entry box for user to enter message
    entry_box = tk.Entry(root,
                         bg="#2C3E50",
                         fg=text_colour,
                         font=font,
                         width=55
                         )
    entry_box.place(x=5,
                    rely=0.925)

    send_button = tk.Button(root,
                            text="Send",
                            font=font_bold,
                            bg="#ABB2B9",
                            command=send,
                            width=10)
    send_button.place(relx=0.77,
                      rely=0.925
                          )


# create_chatbot()

# create a button that will activate the chatbot
def create_chatbot_button(root):
    chatbot_button = tk.Button(root,
                               text="🤖",
                               command=lambda:create_chatbot(root)
                               )
    chatbot_button.pack(side=tk.BOTTOM)

