from itertools import combinations
import re

pattern = re.compile(r'\[([.#]+)]\s(\(.*\))\s\{(.*)}')

total_shortest = 0

for line in open("input.txt"):
    match = re.match(pattern, line.strip())
    if match:
        indicator_lights_match = match.group(1)
        indicator_lights = int("".join(list(map(lambda x: '1' if x == '#' else '0', indicator_lights_match))), 2)

        buttons_match = match.group(2)
        buttons = [list(map(int, button.strip('()').split(','))) for button in buttons_match.split()]
        
        shortest = 0
        for i in range(len(buttons)):
            for combo in combinations(buttons, i + 1):
                lights = 0
                for button in combo:
                    for press in button:
                        lights ^= (1 << len(indicator_lights_match) - 1 - press)
                if lights == indicator_lights:
                    shortest = i + 1
                    break
            if shortest > 0:
                break
        
        total_shortest += shortest

print(total_shortest)
