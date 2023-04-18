def loading_bar(num):
    loading_bar_list = ["."] * 10
    percents_as_symbols = num // 10
    for percent in range(percents_as_symbols):
        loading_bar_list.remove(".")
        loading_bar_list.insert(0, "%")

    return "".join(loading_bar_list)


number = int(input())

if number < 100:
    print(f"{number}% [{loading_bar(number)}]\nStill loading...")
else:
    print(f"{number}% Complete!\n[{loading_bar(number)}]")
