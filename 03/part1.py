joltage = 0

for line in open('input.txt'):
    bank = list(map(int, list(line.strip())))
    bank_size = len(bank)
    first_occurrences = [None] * 9

    for i, rating in enumerate(bank):
        if first_occurrences[rating - 1] is None or i < first_occurrences[rating - 1]:
            first_occurrences[rating - 1] = i
        if rating == 9:
            break

    first_occurrences.reverse()

    for i, first_occurrence in enumerate(first_occurrences):
        if first_occurrence is not None and first_occurrence != bank_size - 1:
            max_rating = 0
            for rating in bank[first_occurrence + 1:]:
                if rating == 9:
                    max_rating = 9
                    break
                else:
                    max_rating = max(rating, max_rating)
            joltage += (9 - i) * 10 + max_rating
            break

print(joltage)
