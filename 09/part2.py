from itertools import combinations

import shapely

tiles = []

for line in open('input.txt'):
    tiles.append(list(map(int, line.strip().split(','))))

p = shapely.Polygon(tiles)

areas = []
for combo in combinations(tiles, 2):
    b = shapely.box(
        min(combo[0][0], combo[1][0]),
        min(combo[0][1], combo[1][1]),
        max(combo[0][0], combo[1][0]),
        max(combo[0][1], combo[1][1]),
    )
    if p.contains(b):
        b2 = shapely.box(
            min(combo[0][0], combo[1][0]),
            min(combo[0][1], combo[1][1]),
            max(combo[0][0], combo[1][0]) + 1,
            max(combo[0][1], combo[1][1]) + 1,
        )
        areas.append((combo, b.area, b2.area))

areas.sort(key=lambda x: x[1], reverse=True)
print(areas[0][2])
