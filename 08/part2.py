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

for pair in distances:
    disjoint_set.merge(pair[0], pair[1])
    if disjoint_set.n_subsets == 1:
        x1 = int(pair[0].split(',')[0])
        x2 = int(pair[1].split(',')[0])
        print(x1 * x2)
        break
