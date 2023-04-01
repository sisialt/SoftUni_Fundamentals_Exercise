while True:
    line = input()
    if line == "stop playing":
        break

    line_args = line.split()
    integers = [int(el.strip()) for el in line_args]

    if len(integers) == len(set(integers)):
        for i in range(len(integers)):
            if integers[i] % 2 == 0:
                integers[i] += 2
        print(f"Unique list: {','.join([str(x) for x in sorted(integers)])}\n"
              f"Output: {sum(integers)/len(integers):.2f}")

    else:
        for i in range(len(integers)):
            if integers[i] % 2 == 1:
                integers[i] += 3
        print(f"Non-unique list: {':'.join([str(x) for x in sorted(integers)])}\n"
              f"Output: {sum(integers)/len(integers):.2f}")
