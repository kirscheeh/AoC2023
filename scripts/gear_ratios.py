#!/usr/bin/env python3

import re

data = open("input/gear_ratios.txt").read().splitlines()

special_symbols = []
numbers=[]
for row, gollum in enumerate(data):
    for index, character in enumerate(gollum):
        #if not character.isdigit() and not character == ".":
        #    special_symbols.append([row, index])
        if character == "*":
            special_symbols.append((row, index))
    for num in re.finditer("[0-9]{1,}", gollum):
        numbers.append((num.group(), row, num.start()))

print(numbers)
result={pos:[] for pos in special_symbols}
for key, *value in numbers:
    row, gollum = value

    gollum_pos = [x for x in range(gollum-1, gollum+len(key)+1)]

    for goll in gollum_pos:
        if (row, goll) in special_symbols:
            result[(row, goll)].append(int(key))
        elif (row-1, goll) in special_symbols:
            result[(row-1, goll)].append(int(key))
        elif (row+1, goll) in special_symbols:
            result[(row+1, goll)].append(int(key))

print(result)

final =[]
for key, value in result.items():
    if len(value) == 2:
        final.append(value[0]*value[1])

print(sum(final))
