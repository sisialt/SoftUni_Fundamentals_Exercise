def all_characters_in_between(ch1, ch2):
    result = []
    for ch in range(ch1 + 1, ch2):
        result.append(chr(ch))
    result = " ".join(result)
    return result


character1 = ord(input())
character2 = ord(input())

print(all_characters_in_between(character1, character2))
