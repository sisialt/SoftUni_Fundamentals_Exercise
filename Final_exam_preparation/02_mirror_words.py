import re

line = input()

mirror_words = []
match_counter = 0

pattern = r"(@|#)(?P<first_word>[A-Za-z]{3,})\1{2}(?P<second_word>[A-Za-z]{3,})\1"

matches = re.finditer(pattern, line)

for match in matches:
    match_counter += 1
    first_word = match.group("first_word")
    second_word = match.group("second_word")
    if first_word == second_word[::-1]:
        mirror = f"{first_word} <=> {second_word}"
        mirror_words.append(mirror)

if not match_counter:
    print(f"No word pairs found!")
else:
    print(f"{match_counter} word pairs found!")

if not mirror_words:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))




#
# import re
#
# line = input()
#
# mirror_words = {}
# match_counter = 0
#
# pattern = r"(@|#)(?P<first_word>[A-Za-z]{3,})\1{2}(?P<second_word>[A-Za-z]{3,})\1"
#
# matches = re.finditer(pattern, line)
#
# for match in matches:
#     match_counter += 1
#     first_word = match.group("first_word")
#     second_word = match.group("second_word")
#     if first_word == second_word[::-1]:
#         mirror_words[first_word] = second_word
#
# if not match_counter:
#     print(f"No word pairs found!")
# else:
#     print(f"{match_counter} word pairs found!")
#
# if not mirror_words:
#     print(f"No mirror words!")
# else:
#     print(f"The mirror words are:")
#     i = 0
#     for word, mirror in mirror_words.items():
#         i += 1
#         if i != len(mirror_words):
#             print(f"{word} <=> {mirror}", end=", ")
#         else:
#             print(f"{word} <=> {mirror}")
#
#
#
