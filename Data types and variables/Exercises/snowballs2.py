snowballs = int(input())

largest_value = 0
output = ""

for i in range(1, snowballs + 1):

    weight_snowball = int(input())
    time_to_the_target = int(input())
    quality_snowball = int(input())

    value_snowball = (weight_snowball // time_to_the_target) ** quality_snowball

    if value_snowball > largest_value:
        largest_value = value_snowball
        output = f"{weight_snowball} : {time_to_the_target} = {value_snowball} ({quality_snowball})"

print(output)
