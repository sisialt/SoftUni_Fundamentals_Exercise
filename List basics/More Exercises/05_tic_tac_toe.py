# def check_who_wins(index, first_player, second_player):
#     if numbers_row1[index] == 1:
#         first_player = True
#         return first_player, second_player
#     elif numbers_row1[index] == 2:
#         second_player = True
#         return first_player, second_player

numbers_row1 = [int(x) for x in input().split()]
numbers_row2 = [int(x) for x in input().split()]
numbers_row3 = [int(x) for x in input().split()]

first_player_wins = False
second_player_wins = False

if numbers_row1[0] == numbers_row1[1] == numbers_row1[2]:
    if numbers_row1[0] == 1:
        first_player_wins = True
    elif numbers_row1[0] == 2:
        second_player_wins = True
if numbers_row2[0] == numbers_row2[1] == numbers_row2[2]:
    if numbers_row2[0] == 1:
        first_player_wins = True
    elif numbers_row2[0] == 2:
        second_player_wins = True
if numbers_row3[0] == numbers_row3[1] == numbers_row3[2]:
    if numbers_row3[0] == 1:
        first_player_wins = True
    elif numbers_row3[0] == 2:
        second_player_wins = True
if numbers_row1[0] == numbers_row2[1] == numbers_row3[2]:
    if numbers_row1[0] == 1:
        first_player_wins = True
    elif numbers_row1[0] == 2:
        second_player_wins = True
if numbers_row1[2] == numbers_row2[1] == numbers_row3[0]:
    if numbers_row1[2] == 1:
        first_player_wins = True
    elif numbers_row1[2] == 2:
        second_player_wins = True

for i in range(0, 3):
    if numbers_row1[i] == numbers_row2[i] == numbers_row3[i]:
        if numbers_row1[i] == 1:
            first_player_wins = True
        elif numbers_row1[i] == 2:
            second_player_wins = True

if first_player_wins:
    print("First player won")
elif second_player_wins:
    print("Second player won")
else:
    print("Draw!")
