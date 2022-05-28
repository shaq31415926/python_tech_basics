while True:
    # create input variables
    num_1 = input("Please enter your first number:")
    operator = input("Please enter an operator of your choice (plus, minus, times, division, floor division, modulus):")
    num_2 = input("Please enter your second number:")

    # casting the input variables
    # make sure floats are inputted
    num_1 = float(num_1)
    num_2 = float(num_2)
    # make sure a string is inputted here
    operator = str(operator)

    # if else if statement to do different operations
    if operator == "plus":
        answer = num_1 + num_2
    elif operator == "minus":
        answer = num_1 - num_2
    elif operator == "times":
        answer = num_1 * num_2
    elif operator == "divide":
        answer = num_1 / num_2
    elif operator == "floor dividision":
        answer = num_1 // num_2
    elif operator == "modulus":
        answer = num_1 % num_2
    else:
        print("My calculator does not do this right now")

    print("The answer is", str(answer)) # print the final answer

    calculate_again = input("Calculate again? Y/N")
    if calculate_again.lower() != "y": # != is not equal
        print("I am going to close the calculator now")
        break
