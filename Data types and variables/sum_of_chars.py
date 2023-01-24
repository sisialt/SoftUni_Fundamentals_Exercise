n = int(input())

total_ascii_sum = 0

for _ in range(n):
    letter = input()
    total_ascii_sum += ord(letter)

print(f"The sum equals: {total_ascii_sum}")