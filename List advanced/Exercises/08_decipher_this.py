message = input(). split()
result = ""
result_as_list = []

for word in message:
    first_letter = []
    word_as_list = []

    for ch in word:
        if ch.isdigit():
            first_letter.append(ch)
            continue
        else:
            word_as_list.append(ch)

    word_as_list[0], word_as_list[-1] = word_as_list[-1], word_as_list[0]

    first = chr(int("".join(first_letter)))
    switched_letters = "".join(word_as_list)

    result = first + switched_letters
    result_as_list.append(result)

print(" ".join(result_as_list))
