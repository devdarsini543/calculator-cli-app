def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero."

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /) or 'x' to exit: ")

    if operation == 'x':
        print("Exiting calculator.")
        break

    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation. Please try again.")
