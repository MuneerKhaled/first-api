# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Simple Calculator")

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = subtract(a, b)
elif operator == "*":
    result = multiply(a, b)
elif operator == "/":
    result = divide(a, b)
else:
    result = "Invalid operator"

print("Result:", result)