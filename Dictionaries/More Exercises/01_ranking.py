# not sorted by points

contests = {}
users = {}

while True:
    line = input()
    if line == "end of contests":
        break

    contest, password = line.split(":")
    contests[contest] = password

while True:
    line = input()
    if line == "end of submissions":
        break

    line_args = line.split("=>")
    contest = line_args[0]
    password = line_args[1]
    username = line_args[2]
    points = int(line_args[3])

    if contest in contests:
        if password == contests[contest]:
            if username not in users:
                users[username] = {"Contest": [], "Points": []}
                users[username]["Contest"].append(contest)
                users[username]["Points"].append(points)
            else:
                if contest in users[username]["Contest"]:
                    index = users[username]["Contest"].index(contest)
                    users[username]["Points"][index] = max(points, users[username]["Points"][index])
                else:
                    users[username]["Contest"].append(contest)
                    users[username]["Points"].append(points)

max_points = 0
best_user = ""

for user in users:
    sum_points = sum(users[user]["Points"])
    if sum_points > max_points:
        max_points = sum_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")

for user in sorted(users):
    print(user)
    for i in range(len(users[user]["Contest"])):
        print(f'#  {users[user]["Contest"][i]} -> {users[user]["Points"][i]}')
