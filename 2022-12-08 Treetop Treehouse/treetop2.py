import sys

def get_viewing_distance(tree, direction):
    dist = 0

    for other_tree in direction:
        dist += 1

        if other_tree >= tree:
            break

    return dist

def get_score(grid, row, col):
    # sets of trees to left, right, above and below
    to_left = grid[row][:col][::-1]
    to_right = grid[row][col + 1:]
    above = [this_row[col] for this_row in grid[:row][::-1]]
    below = [this_row[col] for this_row in grid[row + 1:]]



    # the current tree
    this_tree = grid[row][col]

    a, b, c, d = [get_viewing_distance(this_tree, direction) for direction in [to_left, to_right, above, below]]

    return a * b * c * d


grid = []
top_score = 0

# load grid
for line in sys.stdin:
    grid.append([int(height) for height in line.replace('\n', '')])


for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        score = get_score(grid, row, col)
        if score > top_score:
            top_score = score

print(top_score)
