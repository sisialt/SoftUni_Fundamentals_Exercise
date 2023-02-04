def calculate(operation, n1, n2):
    result = 0
    if operation == "multiply":
        result = n1 * n2
    elif operation == "divide":
        result = n1 // n2
    elif operation == "add":
        result = n1 + n2
    elif operation == "subtract":
        result = n1 - n2
    return result


operator = input()
num1 = int(input())
num2 = int(input())

print(calculate(operator, num1, num2))
