def check_palindrome(num):
    if len(num) == 1:
        return True
    else:
        for i in range(0, len(num) // 2):
            if num[i] == num[-(i + 1)]:
                return True
            else:
                return False


numbers = input().split(", ")

for number in numbers:
    print(check_palindrome(number))

# 12321
