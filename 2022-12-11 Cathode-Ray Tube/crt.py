import sys

x = 1
values = []
total = 0

# process all commands and build list of
# values of x after each cycle
for line in sys.stdin:
    command = line.split()[0]

    if command == 'noop':
        values.append(x)

    if command == 'addx':
        amount = int(line.split()[1])
        values.append(x)
        x += amount
        values.append(x)

# add up strengths for part one
for cycle in range(20, len(values) + 1, 40):
    total += values[cycle - 2] * cycle

print(total)

# draw pixels for part 2
pixels = ['.' for i in range(240)]

for cycle in range(1, len(values) + 1):
    current_x = values[cycle - 1]
    if (cycle % 40) >= current_x - 1 and (cycle % 40) <= current_x + 1:
        pixels[cycle - 1] = '#'

for line_start in range(0, len(pixels), 40):
    for pixel in range(line_start, line_start + 40):
        print(pixels[pixel], end='')
    print()

