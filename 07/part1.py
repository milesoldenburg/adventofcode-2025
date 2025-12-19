from utils.grid import Grid, Direction


grid = Grid('input.txt')

splits = 0

for i in range(grid.column_count):
    for (row, column, value) in grid.walk_row(i):
        if value in ['S', '|']:
            beamed_row, beamed_column, beamed_value = grid.get(i, column, direction=Direction.S)
            if beamed_value == '^':
                splits += 1
                lbeam = grid.get(i, column, direction=Direction.SW)
                if lbeam:
                    if lbeam[2] == '.':
                        grid.set(lbeam[0], lbeam[1], '|')

                rbeam = grid.get(i, column, direction=Direction.SE)
                if rbeam:
                    if rbeam[2] == '.':
                        grid.set(rbeam[0], rbeam[1], '|')
            else:
                grid.set(beamed_row, beamed_column, '|')

print(splits)
