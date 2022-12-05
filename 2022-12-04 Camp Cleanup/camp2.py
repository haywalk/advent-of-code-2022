import sys

overlap = 0

for line in sys.stdin:
    a, b, c, d = [int(i) for i in line.replace('-', ',').split(',')]

    elf_a = set(range(a, b + 1))
    elf_b = set(range(c, d + 1))

    if not elf_a.isdisjoint(elf_b):
        overlap += 1

print(overlap)
