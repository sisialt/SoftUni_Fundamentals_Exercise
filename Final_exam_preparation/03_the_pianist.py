n = int(input())

pieces = {}

for _ in range(n):
    line = input().split("|")
    piece = line[0]
    composer = line[1]
    key = line[2]

    pieces[piece] = [composer, key]

while True:
    line = input()
    if line == "Stop":
        break

    line_args = line.split("|")
    command = line_args[0]
    current_piece = line_args[1]

    if command == "Add":
        current_composer = line_args[2]
        current_key = line_args[3]

        if current_piece in pieces:
            print(f"{current_piece} is already in the collection!")
        else:
            pieces[current_piece] = [current_composer, current_key]
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")

    elif command == "Remove":
        if current_piece in pieces:
            pieces.pop(current_piece)
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = line_args[2]

        if current_piece in pieces:
            pieces[current_piece][1] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

for piece, value in pieces.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")

# forgot line 30
