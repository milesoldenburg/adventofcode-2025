from functools import reduce
from itertools import combinations
import math

from scipy.cluster.hierarchy import DisjointSet

boxes = []

for line in open('input.txt'):
    boxes.append(line.strip())

disjoint_set = DisjointSet(boxes)

distances = []
for combo in combinations(boxes, 2):
    box1 = list(map(int, combo[0].split(',')))
    box2 = list(map(int, combo[1].split(',')))
    distance = math.dist(box1, box2)
    distances.append((combo[0], combo[1], distance))

distances.sort(key=lambda x: x[2])

for pair in distances[:1000]:
    disjoint_set.merge(pair[0], pair[1])

subsets = disjoint_set.subsets()
subsets.sort(key=lambda x: len(x), reverse=True)

lengths = list(map(lambda x: len(x), subsets))[:3]
total = reduce(lambda x, y: x * y, lengths)
print(total)
