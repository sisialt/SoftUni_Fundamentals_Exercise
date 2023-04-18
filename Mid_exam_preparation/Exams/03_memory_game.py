sequence = input().split()

moves = 0
no_more_elements_in_sequence = False

while True:
    command = input()
    if command == "end":
        break

    command_args = command.split()
    first_index = int(command_args[0])
    second_index = int(command_args[1])
    moves += 1

    if first_index == second_index or not 0 <= first_index < len(sequence) or not 0 <= second_index < len(sequence):
        for _ in range(2):
            sequence.insert(len(sequence) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence[first_index] == sequence[second_index]:
        print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
        element = sequence[first_index]
        for _ in range(2):
            sequence.remove(element)
    else:
        print("Try again!")

    if not len(sequence):
        print(f"You have won in {moves} turns!")
        no_more_elements_in_sequence = True
        break

if not no_more_elements_in_sequence:
    print(f'Sorry you lose :(\n{" ".join(sequence)}')
