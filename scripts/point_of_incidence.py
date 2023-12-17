#!/usr/bin/env python

import re
import Levenshtein
from itertools import chain

data = open("input/point_of_incidence.txt").read().split("\n\n")

# replace linebreaks with | symbol
data = [x.replace("\n", "A").replace(".", "0").replace("#", "1") for x in data]

def transpose(data:str) -> list:
    data = data.split("A")
    #data = [x[::-1] for x in data]
    data = list(zip(*data))
    
    data = ["".join(x) for x in data]
    
    data = "A".join(data)
    return data
    

def part1(box) -> int:
    list_pattern = box.split("A")
    length_line = len(list_pattern[0])

    try:
        reflection = re.finditer(r"(?=([01]{{{0}}})A\1)".format(length_line), box)
    except AttributeError:
        return 0

    for x in reflection:
        start = x.start()
        pos = box[:start].count("A")
        before, after = list(reversed(list_pattern[:pos])), list_pattern[pos+2:]

        for be, af in zip(before, after):
            if not be == af:
                break
        else:
            return pos+1
    return 0

def part2(box): #somehow this is random
    lines=box.split("A")
    # get lines with levenshtein distance 0
    changers=set()

    for i1, line1 in enumerate(lines):
        for i2, line2 in enumerate(lines):
            if Levenshtein.distance(line1, line2) == 1:
                if not (i2, i1, line2, line1) in changers:
                    changers.add((i1, i2, line1, line2))
    
    for elem in changers:
        lines[elem[0]] = elem[3]
        new_box = "A".join(lines)
        
        if x:=part1(new_box):
            return x
    return 0
                


result=[]
p2=[]
for pattern in data:
    result.append(part1(pattern)*100+part1(transpose(pattern)))
    p2.append(part2(pattern)*100+part2(transpose(pattern)))
    print(part2(pattern), part2(transpose(pattern)))
    
print("Part 1", sum(result))
print("Part 2", sum(p2))