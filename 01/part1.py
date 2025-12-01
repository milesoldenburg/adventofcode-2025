dial = 50
password = 0

for line in open('input.txt'):
    direction = line[0]
    value = int(line[1:])

    if value >= 100:
        value = value % 100

    if direction == 'L':
        dial -= value
    else:
        dial += value

    if dial < 0:
        dial = 100 - abs(dial)
    elif dial > 99:
        dial = dial - 100

    if dial == 0:
        password += 1

print(password)
