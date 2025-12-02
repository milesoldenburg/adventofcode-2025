invalid_ids_sum = 0

for line in open('input.txt'):
    for r in line.strip().split(','):
        range_start, range_end = map(int, r.split('-'))
        for id in range(range_start, range_end + 1):
            id_s = str(id)
            id_slen = len(id_s)
            if id_slen % 2 == 0:
                if id_s[:id_slen // 2] == id_s[id_slen // 2:]:
                    invalid_ids_sum += id

print(invalid_ids_sum)
