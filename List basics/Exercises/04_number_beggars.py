numbers = input()
beggars = int(input())

list_of_numbers = numbers.split(", ")
list_beggars = [0] * beggars

for i in range(len(list_of_numbers)):
    beggar_idx = i % beggars
    num = int(list_of_numbers[i])
    list_beggars[beggar_idx] += num

print(list_beggars)

    # if i % beggars == 0:
    #     for i in range(len(list_of_numbers) // beggars + 1):
    #         list_beggars.append(list_of_numbers[i])
    #
    #
