#!/usr/bin/env python

import re
from itertools import zip_longest

data = open("input/point_of_incidence.txt").read()

data = data.replace(".", "0").replace("#", "1")
patterns = data.split("\n\n")

patterns= patterns[-1:]

def transpose(data:list) -> list:
    return list(zip(*data))

for pattern in patterns:
    lines = pattern.splitlines()
    
    middle = re.findall(r"^([01]{9})$\n\1", pattern, flags=re.MULTILINE)
    middle_indx = lines.index(middle[0])
    
    print(middle_indx, lines[:middle_indx], lines[middle_indx+2:], len(lines))
    counter=0
    for before, after in zip_longest(reversed(lines[:middle_indx]), lines[middle_indx+2:]):
        if before and after and before == after:
            counter+=1
            
    if counter+middle_indx+1 in [len(lines)-1, len(lines)]:
        print("YES")