def manipulate_input(data_type, num_or_word):
    word_with_symbol = []
    if data_type == "int":
        result = int(num_or_word) * 2
    elif data_type == "real":
        result = f"{float(num_or_word) * 1.5:.2f}"
    elif data_type == "string":
        for el in num_or_word:
            word_with_symbol.append(el)
        word_with_symbol.append("$")
        word_with_symbol.insert(0, "$")
        result = "".join(word_with_symbol)

    return result


input_type = input()
text = input()

print(manipulate_input(input_type, text))
