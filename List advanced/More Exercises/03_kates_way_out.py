def find_way_out(r, c, moves):
    if not (0 <= r < size and 0 <= c < len(matrix[0])):
        return moves

    if matrix[r][c] == "#":
        return 0

    matrix[r][c] = "#"

    result1 = find_way_out(r + 1, c, moves + 1)
    result2 = find_way_out(r - 1, c, moves + 1)
    result3 = find_way_out(r, c + 1, moves + 1)
    result4 = find_way_out(r, c - 1, moves + 1)

    return max(result1, result2, result3, result4)


matrix = []
kate_pos = []

size = int(input())

for row in range(size):
    matrix.append(list(input()))

    if "k" in matrix[row]:
        kate_pos = [row, matrix[row].index("k")]

out_in = find_way_out(kate_pos[0], kate_pos[1], 0)

if not out_in:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {out_in} moves")


# def find_path(pos):
#     possible_way = []
#
#     for dir in directions:
#         next_r, next_c = pos[0] + directions[dir][0], pos[1] + directions[dir][1]
#
#         if 0 <= next_r < len(maze) and 0 <= next_c < len(maze[next_r]):
#
#             if maze[next_r][next_c] == " ":
#                 current_path.append([next_r, next_c])
#                 pos = next_r, next_c
#                 possible_way.append([next_r, next_c])
#
#         else:
#             return current_path
#
#         return find_path(pos)
#
#     return possible_way
#
#
# n = int(input())
#
# maze = []
# kate_position = []
# best_path = []
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
#
# for r in range(n):
#     line = input()
#     maze.append(line)
#
#     if "k" in line:
#         kate_position = (r, line.index("k"))
#
# while True:
#     current_path = []
#
#     result = find_path(kate_position)
#
#     if result == "Kate cannot get out":
#         print("Kate cannot get out")
#         break
#
#     current_path = result
#
#     if len(current_path) > len(best_path):
#         best_path = current_path
