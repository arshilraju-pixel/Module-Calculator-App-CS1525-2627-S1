
# Import calculator functions
from operations import add, subtract, multiply, divide

# Import calculator functions
from operations import add, subtract, multiply, divide

# Import input functions
from utils import get_user_number, get_operation


# Get the first number
number_1 = get_user_number()

# Get the second number
number_2 = get_user_number()

# Get the operation
operation = get_operation()


# Perform the selected calculation
if operation == "+":
    result = add(number_1, number_2)

elif operation == "-":
    result = subtract(number_1, number_2)

elif operation == "*":
    result = multiply(number_1, number_2)

elif operation == "/":

    # Prevent division by zero
    while number_2 == 0:
        print("You cannot divide by zero!")
        print("Please enter a different second number.")
        number_2 = get_user_number()

    result = divide(number_1, number_2)


# Display the calculation and result
print("Calculation:", number_1, operation, number_2)
print("Result:", result)
