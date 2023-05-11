import os

# code to clear the screen
os.system("clear")
print("Hello! This is my calculator in Python")

num1 = input("Please enter the first number:")
operator = input("Please enter the operator (+, -, *, /):")
num2 = input("Please enter the second number:")

# convert the variables to float
num1 = float(num1)
num2 = float(num2)

if operator == "+":
    total = num1 + num2
    print("The total is", round(total, 2))
elif operator == "-":
    total = num1 - num2
    print("The total is", round(total, 2))
elif operator == "*":
    total = num1 * num2
    print("The total is", round(total, 2))
elif operator == "/":
    total = num1 / num2
    print("The total is", round(total, 2))
else:
    print("Operator not found")

