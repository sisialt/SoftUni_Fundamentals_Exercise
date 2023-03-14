input_data = input()

message = ""

while input_data:
    for ch in input_data:

        if ch.isdigit():

            idx = input_data.index(ch)
            result = input_data[:idx]
            number = int(ch)

            if idx != len(input_data) - 1:
                if input_data[idx + 1].isdigit():
                    number = int(ch + input_data[idx + 1])

            for _ in range(number):
                message += result.upper()

            input_data = input_data[idx + 1:]

            break

print(f"Unique symbols used: {len(set(message))}")
print(message)
