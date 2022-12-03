import sys

def response(opponent, outcome):
    if outcome == 1:
        return opponent

    elif outcome == 2:
        return (opponent + 1) % 3

    else:
        return (opponent + 2) % 3

score = 0

for line in sys.stdin:

    opponent = ord(line[0]) - 65
    outcome = ord(line[2]) - 88

    score += 3 * outcome + 1 + response(opponent, outcome);

print(score)
