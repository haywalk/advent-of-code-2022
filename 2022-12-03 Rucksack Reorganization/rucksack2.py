import sys

total = 0
group = []

for line in sys.stdin:
    group.append(set(line.replace('\n', '')))

    if len(group) == 3:
        badge = group[0].intersection(group[1].intersection(group[2])).pop()
        group.clear()

        if ord(badge) > ord('a'):
            total += ord(badge) - ord('a') + 1
        else:
            total += ord(badge) - ord('A') + 27

print(total)
