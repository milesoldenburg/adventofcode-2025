from utils.grid import Grid, Direction


grid = Grid('input.txt')

shadow_grid = []
for i in range(grid.row_count):
    shadow_grid.append([0] * grid.column_count)

for i in range(grid.column_count):
    for (row, column, value) in grid.walk_row(i):
        if value in ['S', '|']:
            beamed_row, beamed_column, beamed_value = grid.get(i, column, direction=Direction.S)
            if beamed_value == '^':
                lbeam = grid.get(i, column, direction=Direction.SW)
                if lbeam:
                    if lbeam[2] != '^':
                        grid.set(lbeam[0], lbeam[1], '|')
                        shadow_grid[lbeam[0]][lbeam[1]] += shadow_grid[row][column]

                rbeam = grid.get(i, column, direction=Direction.SE)
                if rbeam:
                    if rbeam[2] != '^':
                        grid.set(rbeam[0], rbeam[1], '|')
                        shadow_grid[rbeam[0]][rbeam[1]] += shadow_grid[row][column]
            else:
                grid.set(beamed_row, beamed_column, '|')
                shadow_grid[beamed_row][beamed_column] += max(1, shadow_grid[row][column])

print(sum(shadow_grid[grid.row_count - 1]))
