def factorial(num):
    factorial_num = 1
    for i in range(1, num + 1):
        factorial_num *= i

    return factorial_num


def divide_factorials(n1, n2):
    result = factorial(n1) / factorial(n2)
    return result


num1 = int(input())
num2 = int(input())

print(f"{divide_factorials(num1, num2):.2f}")
