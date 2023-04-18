def is_perfect_number(num):
    divisors = []
    is_perfect = False

    for n in range(1, number // 2 + 1):
        if number % n == 0:
            divisors.append(n)

    if sum(divisors) == number:
        is_perfect = True

    return is_perfect


number = int(input())

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


