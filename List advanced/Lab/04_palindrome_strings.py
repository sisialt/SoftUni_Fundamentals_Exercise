words = input().split()
palindrome = input()

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(palindrome)} times")
