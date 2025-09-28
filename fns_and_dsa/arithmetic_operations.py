# File: arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Parameters:
        num1: float, first number
        num2: float, second number
        operation: str, one of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: Result of the operation or a string indicating an error
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
