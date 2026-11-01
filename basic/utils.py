
def get_user_number() -> float:
    """
    Asks the user to enter a number and validates the input.

    Returns:
        A valid number entered by the user.
    """
    while True:
        try:
            number = float(input("Enter a number: "))
            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operation() -> str:
    """
    Asks the user to choose a mathematical operation.

    Returns:
        A valid operation symbol (+, -, *, or /).
    """
    while True:
        operation = input("Choose an operation (+, -, *, /): ")

        if operation in ["+", "-", "*", "/"]:
            return operation

        else:
            print("Invalid operation! Please choose +, -, *, or /.")
