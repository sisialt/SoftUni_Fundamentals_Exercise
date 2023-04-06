import re

food_info = input()

total_calories = 0
foods = []
foods_dict = {}

pattern = r"(#|\|)(?P<Item>[A-Za-z ]+)\1" \
          r"(?P<ExpirationDate>\d{2}/\d{2}/\d{2})\1" \
          r"(?P<Calories>[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9]|[1-9]*[0-9])\1"

# match_results = re.findall(pattern, food_info)
#
# for match in match_results:
#     total_calories += int(match[3])
#     food = f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}"
#     foods.append(food)
# print(f"You have food to last you for: {total_calories//2000} days!")
#
# for food in foods:
#     print(food)

match_results = re.finditer(pattern, food_info)

for match in match_results:
    foods_dict = match.groupdict()
    total_calories += int(match['Calories'])
    res = f"Item: {match['Item']}, Best before: {match[2]}, Nutrition: {foods_dict['Calories']}"
    foods.append(res)

print(f"You have food to last you for: {total_calories//2000} days!")

for food in foods:
    print(food)
