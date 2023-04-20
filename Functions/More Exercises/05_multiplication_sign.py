def find_multiplication(n1, n2, n3):

    list_nums = [n1, n2, n3]
    negatives_counter = 0

    for num in list_nums:
        if num < 0:
            negatives_counter += 1

    if negatives_counter % 2 == 0:
        return True
    else:
        return False


num1 = int(input())
num2 = int(input())
num3 = int(input())

if find_multiplication(num1, num2, num3):
    if num1 and num2 and num3:
        print("positive")
    else:
        print("zero")
else:
    print("negative")