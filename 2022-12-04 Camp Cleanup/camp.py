import sys

overlap = 0

for line in sys.stdin:
    a = int(line.split(',')[0].split('-')[0])
    b = int(line.split(',')[0].split('-')[1])
    c = int(line.split(',')[1].split('-')[0])
    d = int(line.split(',')[1].split('-')[1])

    elf_a = set(range(a, b + 1))
    elf_b = set(range(c, d + 1))

    if elf_a.issubset(elf_b) or elf_b.issubset(elf_a):
        overlap += 1

print(overlap)
