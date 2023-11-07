def add_numbers(num1, num2):
    """This function adds two numbers"""

    total = num1 + num2

    return total


def subtract_numbers(num1, num2):
    """This function subtract two numbers"""

    total = num1 - num2

    return total


def multiply_numbers(num1, num2):
    """This function multiplies two numbers"""

    total = num1 * num2

    return total


def divide_numbers(num1, num2):
    """This function divides two numbers.
    This will give an error if the second number is zero"""

    if num2 == 0:
        total = "Error"
    else:
        total = round(num1 / num2, 2)
    return total


num1 = int(input("What is the first number?:"))
num2 = int(input("What is the second number?:"))
operator = input("What operator would you like to use? [+, -, *, /]:")

if operator == "+":
    total = add_numbers(num1, num2)
elif operator == "-":
    total = subtract_numbers(num1, num2)
elif operator == "*":
    total = multiply_numbers(num1, num2)
elif operator == "/":
    total = divide_numbers(num1, num2)
else:
    total = "Error"

print(f"The answer is {total}")
