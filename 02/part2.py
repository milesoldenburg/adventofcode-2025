invalid_ids_sum = 0

for line in open('input.txt'):
    for r in line.strip().split(','):
        range_start, range_end = map(int, r.split('-'))
        for id in range(range_start, range_end + 1):
            id_s = str(id)
            id_slen = len(id_s)

            for blocksize in range(1, id_slen // 2 + 1):
                if id_slen % blocksize == 0:
                    blocks = []
                    for block in range(0, id_slen - blocksize + 1, blocksize):
                        blocks.append(id_s[block:(block + blocksize)])

                    if len(set(blocks)) == 1:
                        invalid_ids_sum += id
                        break

print(invalid_ids_sum)
