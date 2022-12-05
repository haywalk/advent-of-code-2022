import sys

def parse_line(line):
    # starting at the second character, every fourth
    # character is important
    return [i for i in line[1::4]]

def parse_stacks(lines):
    # list of empty lists (stacks)
    stacks = [[] for i in range(len(lines[0]))]

    # start adding from the bottom
    for line in lines[::-1]:
        # add element i from each line to stack i
        for i in range(len(line)):
            if(line[i] != ' '):
                stacks[i].append(line[i])

    return stacks

def execute_command(stacks, command):
    # get data from the command string
    num_to_move, stack_from, stack_to = [int(i) for i in command.split(' ')[1::2]]

    for move in range(num_to_move):
        stacks[stack_to - 1].append(stacks[stack_from - 1].pop())

stacks = []
lines_of_input = []
started = False
result = ''

for line in sys.stdin:
    # after all the stacks have been entered, parse them
    if not started and '[' not in line:
        started = True
        stacks = parse_stacks(lines_of_input)

    # skip the blank line
    elif line == '\n':
        continue

    # if this line is part of a stack, parse it
    elif not started:
        lines_of_input.append(parse_line(line))

    # otherwise this is a command, so execute it
    else:
        execute_command(stacks, line)

# print result
for stack in stacks:
    if(len(stack) > 0):
        result += stack[-1]
    else:
        result += ' '

print(result)
