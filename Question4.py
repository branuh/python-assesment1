# Prompt the user to enter two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")
# Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation")
    result = None

# Print the result
if result is not None:
    print("Result:", result)