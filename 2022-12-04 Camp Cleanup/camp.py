import sys

overlap = 0

for line in sys.stdin:
    a, b, c, d = [int(i) for i in line.replace('-', ',').split(',')]

    elf_a = set(range(a, b + 1))
    elf_b = set(range(c, d + 1))

    if elf_a.issubset(elf_b) or elf_b.issubset(elf_a):
        overlap += 1

print(overlap)
