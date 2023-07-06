# illustration of the Guardian Pattern
def divide_numbers(a, b):
    if b != 0:  # Guardian condition to prevent division by zero
        result = a / b
        print("The division result is:", result)
    else:
        print("Oops! Division by zero is not allowed.")

# Example usage
divide_numbers(10, 2)  # Output: The division result is: 5.0
divide_numbers(10, 0)  # Output: Oops! Division by zero is not allowed.
