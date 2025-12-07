fresh_ranges = []

for line in open('input-fresh.txt'):
    fresh_ranges.append(list(map(int, line.strip().split('-'))))

fresh_ranges.sort(key=lambda x: x[0])
merged_ranges = [fresh_ranges[0]]

for fresh_range in fresh_ranges[1:]:
    last_merged = merged_ranges[-1]

    if fresh_range[0] <= last_merged[1]:
        last_merged[1] = max(last_merged[1], fresh_range[1])
    else:
        merged_ranges.append(fresh_range)

total_fresh_ingredients = 0

for merged_range in merged_ranges:
    total_fresh_ingredients += merged_range[1] - merged_range[0] + 1

print(total_fresh_ingredients)
