from utils.grid import Grid


grid = Grid('test.txt')

accessible_rolls = 0

for rowi, columni, value in grid.walk():
    if value == '.':
        continue

    adjacencies = grid.adjacencies(rowi, columni)

    adjacent_rolls = 0
    for adjacency in adjacencies.values():
        if adjacency == '@':
            adjacent_rolls += 1

    if adjacent_rolls < 4:
        accessible_rolls += 1

print(accessible_rolls)
