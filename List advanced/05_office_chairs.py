rooms = int(input())

total_free_chairs = 0
result = ""
are_enough_chairs = True

for room in range(1, rooms + 1):
    chairs_vs_visitors = input().split()

    chairs = chairs_vs_visitors[0]
    visitors = int(chairs_vs_visitors[1])
    needed_chairs = 0

    if len(chairs) >= visitors:
        total_free_chairs += len(chairs) - visitors
    else:
        are_enough_chairs = False
        needed_chairs = visitors - len(chairs)
        result += f"{needed_chairs} more chairs needed in room {room}\n"

if are_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
else:
    print(result)
    