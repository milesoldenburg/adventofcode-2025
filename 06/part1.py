from functools import reduce


problems = []
operations = []
grand_total = 0

for i in range(1000):
    problems.append([])

for line in open('input-numbers.txt'):
    for i, value in enumerate(list(map(int, line.strip().split()))):
        problems[i].append(value)

for line in open('input-operations.txt'):
    operations = line.strip().split()

for i, problem in enumerate(problems):
    if operations[i] == '+':
        total = sum(problem)
    else:
        total = reduce(lambda x, y: x * y, problem)

    grand_total += total

print(grand_total)
