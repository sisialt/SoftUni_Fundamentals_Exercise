snowballs = int(input())

largest_value = 0
best_weight_snowball = 0
best_time_to_the_target = 0
best_quality_snowball = 0

for i in range(1, snowballs + 1):

    weight_snowball = int(input())
    time_to_the_target = int(input())
    quality_snowball = int(input())

    value_snowball = (weight_snowball / time_to_the_target) ** quality_snowball

    if i == 1 or value_snowball > largest_value:
        largest_value = value_snowball
        best_weight_snowball = weight_snowball
        best_time_to_the_target = time_to_the_target
        best_quality_snowball = quality_snowball

print(f"{best_weight_snowball} : {best_time_to_the_target} = {int(largest_value)} ({best_quality_snowball})")
