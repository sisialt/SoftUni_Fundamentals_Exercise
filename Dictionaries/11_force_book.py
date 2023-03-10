force_book_by_side = {}
force_book_by_users = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        force_side, force_user = line.split(" | ")
        if force_user in force_book_by_users:
            continue

        if force_side not in force_book_by_side:
            force_book_by_side[force_side] = []

        force_book_by_users[force_user] = force_side
        force_book_by_side[force_side].append(force_user)

    elif " -> " in line:
        force_user, force_side = line.split(" -> ")

        if force_side not in force_book_by_side:
            force_book_by_side[force_side] = []

        force_book_by_side[force_side].append(force_user)

        if force_user in force_book_by_users:
            force_book_by_side[force_book_by_users[force_user]].remove(force_user)

        print(f"{force_user} joins the {force_side} side!")


for side, users in force_book_by_side.items():
    if len(users):
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

# lines 23-26 before 28-29
