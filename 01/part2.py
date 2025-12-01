dial = 50
password = 0

for line in open('test.txt'):
    starting_dial = dial
    direction = line[0]
    value = int(line[1:])

    if value >= 100:
        q, r = divmod(value, 100)
        value = r
        password += q

    if direction == 'L':
        dial -= value
    else:
        dial += value

    if dial == 0:
        password += 1
    elif dial < 0:
        dial = 100 - abs(dial)
        if starting_dial != 0:
            password += 1
    elif dial > 99:
        dial -= 100
        if starting_dial != 0:
            password += 1

print(password)
