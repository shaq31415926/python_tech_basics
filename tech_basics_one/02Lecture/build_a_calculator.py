# The input() function allows user input.
# Ask the user to input two numbers and operator

num1 = input("Please enter the First Number:\n")
operator = input("Please specify the Operator (+, -, *, /):\n")
num2 = input("Please enter the Second Number:\n")

# convert the number to float
num1 = float(num1)
num2 = float(num2)

# if else if statement to carry out different operations
# we use == in python
if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2

# print the final answer and convert the output to str
print("The answer is: " + str(out))