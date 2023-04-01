from datetime import date

info_date = input().split("-")
year, month, day = int(info_date[0]), int(info_date[1]), int(info_date[2])

today = date(2018, 8, 26)
input_date = date(year, month, day)

delta = input_date - today

if delta.days < 0:
    print("Passed")
elif delta.days == 0:
    print("Today date")
else:
    print(f"{delta.days + 1} days left")
