followers = {}

while True:
    line = input()
    if line == "Log out":
        break

    line_args = line.split(": ")
    command = line_args[0]
    username = line_args[1]

    if command == "New follower":
        if username not in followers:
            followers[username] = {"Likes": 0, "Comments": 0}

    elif command == "Like":
        count = int(line_args[2])

        if username not in followers:
            followers[username] = {"Likes": count, "Comments": 0}
        else:
            followers[username]["Likes"] += count

    elif command == "Comment":
        if username not in followers:
            followers[username] = {"Likes": 0, "Comments": 1}
        else:
            followers[username]["Comments"] += 1

    elif command == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)

print(f"{len(followers)} followers")

for follower, values in followers.items():
    sum_likes_and_comments = values["Likes"] + values["Comments"]
    print(f"{follower}: {sum_likes_and_comments}")


# def is_username_in_followers(user, seq):
#     if user in seq:
#         return True
#     return False
#
#
# followers = {}
#
# while True:
#     line = input()
#     if line == "Log out":
#         break
#
#     line_args = line.split(": ")
#     command = line_args[0]
#     username = line_args[1]
#
#     if command == "New follower":
#         if not is_username_in_followers(username, followers):
#             followers[username] = {"Likes": 0, "Comments": 0}
#
#     elif command == "Like":
#         count = int(line_args[2])
#         if not is_username_in_followers(username, followers):
#             followers[username] = {"Likes": count, "Comments": 0}
#         else:
#             followers[username]["Likes"] += count
#
#     elif command == "Comment":
#         if not is_username_in_followers(username, followers):
#             followers[username] = {"Likes": 0, "Comments": 1}
#         else:
#             followers[username]["Comments"] += 1
#
#     elif command == "Blocked":
#         if not is_username_in_followers(username, followers):
#             print(f"{username} doesn't exist.")
#         else:
#             followers.pop(username)
#
# print(f"{len(followers)} followers")
#
# for follower, values in followers.items():
#     sum_likes_and_comments = values["Likes"] + values["Comments"]
#     print(f"{follower}: {sum_likes_and_comments}")
#
