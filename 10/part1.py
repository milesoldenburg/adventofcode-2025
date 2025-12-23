import re

pattern = re.compile(r'\[([\.#]+)\]\s(\(.*\))\s\{(.*)\}')

for line in open("test.txt"):
    match = re.match(pattern, line.strip())
    if match:
        indicator_lights_match = match.group(1)
        indicator_lights = int("".join(list(map(lambda x: '1' if x == '#' else '0', indicator_lights_match))), 2)

        buttons_match = match.group(2)
        buttons = [list(map(int, button.strip('()').split(','))) for button in buttons_match.split()]
