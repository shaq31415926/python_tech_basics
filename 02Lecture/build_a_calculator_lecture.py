while True:
    # create two numerical variables that the user can input
    num_1 = input("Please enter First number:")
    num_2 = input("Please enter Second number:")
    # create an operator variable that the user can input
    operator = input("Please select an Operator (+, -, *, /):")

    # convert the numbers to float
    num_1 = float(num_1)
    num_2 = float(num_2)

    # if else if statement to carry out different operazions
    # don't forget we use == in Python

    if operator == "+":
        out = num_1 + num_2
    elif operator == "-":
        out = num_1 - num_2
    elif operator == "*":
        out = num_1*num_2
    elif operator == "/":
        out = num_1/num_2

    # print out the final answer
    # convert the final answer to string
    out = round(out, 2) # round the output to two digits
    print("The Answer is: " + str(out))

    # if you input N the calculator will exit. If you input Y the calculator will run again.
    calculate_again = input("Calculate again? (Y/N): ")
    if calculate_again.lower() != "y": # != is not equal and lower takes the input of variables and lowers it
         break
