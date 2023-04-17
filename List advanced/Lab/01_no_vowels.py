text = input()
forbidden_vowels = ['a', 'o', 'u', 'e', 'i']

result = [ch for ch in text if ch.lower() not in forbidden_vowels]

print("".join(result))