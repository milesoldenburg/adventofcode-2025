from functools import reduce


grand_total = 0

rows = []
for line in open('input-numbers.txt'):
    rows.append(line.strip('\n'))

for line in open('input-operations.txt'):
    operator = None
    problem = []
    for i, c in enumerate(line.strip('\n')):
        if c in ['+', '*']:
            operator = c
            
        digits = ''
        for row in rows:
            if row[i] != ' ':
                digits += row[i]
                
        if digits == '':
            if operator == '+':
                total = sum(problem)
            else:
                total = reduce(lambda x, y: x * y, problem)

            grand_total += total
            operator = None
            problem = []
        else:
            problem.append(int(digits))

    if operator == '+':
        total = sum(problem)
    else:
        total = reduce(lambda x, y: x * y, problem)

    grand_total += total
            
print(grand_total)
