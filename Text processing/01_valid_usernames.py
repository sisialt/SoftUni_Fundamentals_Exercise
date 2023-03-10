usernames = input().split(", ")

for username in usernames:
    is_valid = True
    if 3 <= len(username) <= 16:
        for ch in username:
            if not (ch.isalnum() or ch == "-" or ch == "_"):
                is_valid = False
                break
        if is_valid:
            print(f"{username}")
    else:
        continue
