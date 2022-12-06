import sys

def solve(message, size):
    index = 0

    while len(set(message[index:index + size])) != size:
            index += 1

    return index + size

message = ''

for line in sys.stdin:
    message += line.replace('\n', '')

# part one
print(solve(message, 4))

# part two
print(solve(message, 14))
