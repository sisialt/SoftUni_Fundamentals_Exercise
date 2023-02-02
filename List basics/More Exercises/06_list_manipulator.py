numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break

    command = command.split()

    even_numbers = [i for i in numbers if i % 2 == 0]
    odd_numbers = [i for i in numbers if i % 2 != 0]
    first_list, last_list = [], []

    if command[0] == "exchange":
        if int(command[1]) >= len(numbers) or int(command[1]) < 0:
            print("Invalid index")
        else:
            for i in range(int(command[1]) + 1):
                numbers.append(numbers[i])
            for i in range(int(command[1]) + 1):
                numbers.pop(0)

    elif command[0] == "max":
        if command[1] == "even":
            if len(even_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(max(even_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")
        elif command[1] == "odd":
            if len(odd_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(max(odd_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            if len(even_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(min(even_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")
        elif command[1] == "odd":
            if len(odd_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(min(odd_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")

    elif command[0] == "first":
        if int(command[1]) > len(numbers) or int(command[1]) <= 0:
            print("Invalid count")
            continue

        if command[2] == "even":
            if int(command[1]) <= len(even_numbers):
                for i in range(0, int(command[1])):
                    first_list.insert(i, even_numbers[i])
                print(first_list)
            else:
                print(even_numbers)
        elif command[2] == "odd":
            if int(command[1]) <= len(odd_numbers):
                for i in range(0, int(command[1])):
                    first_list.insert(i, odd_numbers[i])
                print(first_list)
            else:
                print(odd_numbers)

    elif command[0] == "last":
        if int(command[1]) > len(numbers) or int(command[1]) <= 0:
            print("Invalid count")
            continue

        if command[2] == "even":
            if int(command[1]) <= len(even_numbers):
                for i in range(0, int(command[1])):
                    last_list.insert(i, even_numbers[len(even_numbers) - int(command[1]) + i])
                print(last_list)
            else:
                print(even_numbers)

        elif command[2] == "odd":
            if int(command[1]) <= len(odd_numbers):
                for i in range(0, int(command[1])):
                    last_list.insert(i, odd_numbers[len(odd_numbers) - int(command[1]) + i])
                print(last_list)
            else:
                print(odd_numbers)

print(numbers)

# 1 10 100 1000
# exchange 3
# first 2 odd
# last 2 even
# end
#
# bugs: line 83 (91) index of element in last_list - even_numbers[i] -> even_numbers[len(even_numbers) ->
# int(command[1]) + i] line 56 (76) forgot negative count and 0 line 15 forgot negative index
# lines 10-13 first, last, even, odd every loop new
