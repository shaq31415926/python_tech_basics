# Definition to calculate area
import os
os.system("clear") # code to clear the terminal for mac users

def calc_rectangle_area(height, width):
    """This definition calculates the area of a rectangle"""

    area = height * width

    return area

height = int(input("What is the height in cm?:"))  # converts the input to an integer
width = int(input("What is the width in cm?:"))
area = calc_rectangle_area(height, width)

print(f"The area of the rectangle is {area} cm2")
