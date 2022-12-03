import sys

total = 0

# 97-122 (a-z): 1-26
# 65-90 (A-Z): 27-52

for line in sys.stdin:
    first_compartment = set(line[:len(line) // 2])
    second_compartment = set(line[len(line) // 2:])
    overlap = first_compartment.intersection(second_compartment)

    for item in overlap:
        if ord(item) > ord('a'):
            total += ord(item) - ord('a') + 1
        else:
            total += ord(item) - ord('A') + 27

print(total)
