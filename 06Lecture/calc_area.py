# Definition to calculate area
# credit to E(??) for inspiring this code

height = input("What is the height?")
width = input("What is the width?")


def calc_area(height, width):
    """This definition calculates the area"""

    area= height*width

    return area

area = calc_area(height, width)

print("The area of the rectangle is:", area)
