import sys

def result(opponent, response):

    if opponent == response:
        return 1

    if (opponent + 1) % 3 == response:
        return 2

    return 0

score = 0

for line in sys.stdin:
    opponent = ord(line[0]) - 65
    response = ord(line[2]) - 88

    score += response + 1 + 3 * result(opponent, response)

print(score)
