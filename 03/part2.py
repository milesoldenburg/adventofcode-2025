total_joltage = 0

for line in open('input.txt'):
    bank = list(map(int, list(line.strip())))
    bank_size = len(bank)

    joltage = []
    sub_bank_start = 0

    while len(joltage) < 12:
        first_occurrences = [None] * 9

        sub_bank_end = bank_size - 12 + len(joltage) + 1

        sub_bank = bank[sub_bank_start:sub_bank_end]

        for i, rating in enumerate(sub_bank):
            if first_occurrences[rating - 1] is None or i < first_occurrences[rating - 1]:
                first_occurrences[rating - 1] = i
            if rating == 9:
                break

        first_occurrences.reverse()

        for i, first_occurrence in enumerate(first_occurrences):
            if first_occurrence is not None and first_occurrence != len(sub_bank):
                max_rating = 0
                for rating in sub_bank[first_occurrence:]:
                    if rating == 9:
                        max_rating = 9
                        break
                    else:
                        max_rating = max(rating, max_rating)
                joltage.append(max_rating)
                sub_bank_start += 1 + first_occurrence
                break

    joltage = map(str, joltage)
    joltage = "".join(joltage)
    joltage = int(joltage)
    total_joltage += joltage

print(total_joltage)
