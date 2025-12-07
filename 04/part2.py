from utils.grid import Grid


grid = Grid('input.txt')

total_rolls_removed = 0

while True:
    rolls_to_remove = []

    for rowi, columni, value in grid.walk():
        if value == '.':
            continue

        adjacencies = grid.adjacencies(rowi, columni)

        adjacent_rolls = 0
        for adjacency in adjacencies.values():
            if adjacency == '@':
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            rolls_to_remove.append((rowi, columni))

    total_rolls_removed += len(rolls_to_remove)

    if len(rolls_to_remove) == 0:
        break

    for rowi, columni in rolls_to_remove:
        grid.grid[rowi][columni] = '.'

print(total_rolls_removed)
