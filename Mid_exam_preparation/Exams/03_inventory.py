def is_in_journal(seq, sequence):
    if seq in sequence:
        return True
    return False


journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    action, item = command.split(" - ")

    if action == "Collect":
        if not is_in_journal(item, journal):
            journal.append(item)

    elif action == "Drop":
        if is_in_journal(item, journal):
            journal.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if is_in_journal(old_item, journal):
            journal.insert(journal.index(old_item) + 1, new_item)

    elif action == "Renew":
        if is_in_journal(item, journal):
            idx = journal.index(item)
            journal.append(item)
            journal.pop(idx)

print(*journal, sep=", ")
