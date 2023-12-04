#!/usr/bin/env python

import math
import re
data = open("input/scratchcards.txt").read().splitlines()

results=[]

queue= []
values={}

for line in data:
    cards, numbers = line.split(":")
    cards = re.findall("[0-9]{1,}", cards)
    winning, yours = numbers.split("|")
    winning = [x for x in winning.strip().split(" ") if not x == ""]
    yours = [x for x in yours.strip().split(" ") if not x == ""]
    
    winning = set(winning)
    yours = set(yours)
    
    num_match = len(winning.intersection(yours))
    queue.append((int(cards[0]), num_match))
    values[int(cards[0])] = num_match
    points = 2**(num_match-1) if num_match > 0 else 0
    results.append(points)
    
print("Part 1", sum(results))

results=[]

cards = 0

while queue:
    card, val = queue.pop()
    
    for i in range(card+1, card+val+1):
        queue.append((i, values[i]))

    cards+=1
        
print("Part 2", cards)