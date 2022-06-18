from clint.textui import puts, colored

bot_name = "Bob"
puts(colored.cyan(f"Hey! I'm {bot_name} :)"))

username = input("Let's start.. What is your name?")
puts(colored.cyan(f"Hi {username}! How are you?"))

response = input()
puts(colored.cyan(f"Got your message! You said {response}"))
