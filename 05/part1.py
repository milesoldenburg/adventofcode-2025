fresh_ranges = []

for line in open('input-fresh.txt'):
    fresh_ranges.append(list(map(int, line.strip().split('-'))))

fresh_ingredients = 0

for line in open('input-available.txt'):
    ingredient_id = int(line.strip())

    for fresh_range in fresh_ranges:
        if ingredient_id in range(fresh_range[0], fresh_range[1] + 1):
            fresh_ingredients += 1
            break

print(fresh_ingredients)
