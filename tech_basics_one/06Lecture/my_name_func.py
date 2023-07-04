def my_name_function(first_name, middle_name, last_name):
    """This definition prints the name"""

    if middle_name is None:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} {middle_name} {last_name}")


my_name_function(first_name="Sarah", middle_name=None, last_name="Haq")
