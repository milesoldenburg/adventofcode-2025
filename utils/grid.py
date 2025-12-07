from enum import Enum


class Direction(Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8


class Grid:
    grid = []
    row_count = 0
    column_count = 0

    def __init__(self, filename):
        for line in open(filename):
            self.grid.append([*line.strip()])
            self.row_count += 1

        self.column_count = len(self.grid[0])

    def walk(self):
        for rowi, row in enumerate(self.grid):
            for columni, column in enumerate(row):
                yield (rowi, columni, column)

    def adjacencies(self, rowi, columni):
        adjacencies = {}
        for direction in Direction:
            adjacencies[direction] = self.get(rowi, columni, direction=direction)
        return adjacencies

    def get(self, rowi, columni, direction=None):
        if direction == Direction.N:
            if rowi - 1 >= 0:
                return self.get(rowi - 1, columni)
            else:
                return None
        elif direction == Direction.NE:
            if rowi - 1 >= 0 and columni + 1 < len(self.grid[rowi]):
                return self.get(rowi - 1, columni + 1)
            else:
                return None
        elif direction == Direction.E:
            if columni + 1 < len(self.grid[rowi]):
                return self.get(rowi, columni + 1)
            else:
                return None
        elif direction == Direction.SE:
            if rowi + 1 < len(self.grid) and columni + 1 < len(self.grid[rowi]):
                return self.get(rowi + 1, columni + 1)
            else:
                return None
        elif direction == Direction.S:
            if rowi + 1 < len(self.grid):
                return self.get(rowi + 1, columni)
            else:
                return None
        elif direction == Direction.SW:
            if rowi + 1 < len(self.grid) and columni - 1 >= 0:
                return self.get(rowi + 1, columni - 1)
            else:
                return None
        elif direction == Direction.W:
            if columni - 1 >= 0:
                return self.get(rowi, columni - 1)
            else:
                return None
        elif direction == Direction.NW:
            if rowi - 1 >= 0 and columni - 1 >= 0:
                return self.get(rowi - 1, columni - 1)
            else:
                return None
        else:
            return self.grid[rowi][columni]

    def print(self):
        for row in self.grid:
            print(row)
