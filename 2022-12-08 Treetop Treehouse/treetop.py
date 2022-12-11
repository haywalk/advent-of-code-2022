import sys

def is_visible(grid, row, col):
    # sets of trees to left, right, above and below
    to_left = grid[row][:col]
    to_right = grid[row][col + 1:]
    above = [this_row[col] for this_row in grid[:row]]
    below = [this_row[col] for this_row in grid[row + 1:]]

    # the current tree
    this_tree = grid[row][col]

    return (this_tree > max(above)) or\
            (this_tree > max(below)) or\
            (this_tree > max(to_left)) or\
            (this_tree > max(to_right))

grid = []
visible = 0

# load grid
for line in sys.stdin:
    grid.append([int(height) for height in line.replace('\n', '')])

# add up edge trees
visible += 2 * len(grid) + 2 * (len(grid[0]) - 2)

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if is_visible(grid, row, col):
            visible += 1

print(visible)
