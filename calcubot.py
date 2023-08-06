import mainbot

def main():
    try:
        equation = input("\nWhat do you need me to calculate? ")
        response = solve_equation(equation)
        print("Answer: " + response)
    except Exception as e:
        print("An error occurred:", e)

    exit = input("Would you like to exit calcubot?(yes/no)")
    if exit.lower() == "yes":
        mainbot.robo()
    else:
        main()

def solve_equation(equation):
    result = eval(equation)  # Use eval to directly evaluate the arithmetic expression
    return str(result)

if __name__ == "__main__":
    main()
