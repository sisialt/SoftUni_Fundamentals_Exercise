needed_experience = float(input())
battles = int(input())

total_experience = 0

for battle in range(1, battles + 1):
    experience_per_battle = float(input())

    if battle % 15 == 0:
        experience_per_battle *= 1.05
    else:
        if battle % 3 == 0:
            experience_per_battle *= 1.15

        if battle % 5 == 0:
            experience_per_battle *= 0.90

    total_experience += experience_per_battle

    if total_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

else:
    print(f"Player was not able to collect the needed experience, {needed_experience - total_experience:.2f} more needed.")
