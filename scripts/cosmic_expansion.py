#!/usr/bin/env python
import numpy as np

data = open("input/cosmic_expansion.txt").read().splitlines()

# build expansion
def find_rows(data) -> list:
    interest = []
    for index, row in enumerate(data):
        if row.count("#") == 0:
            interest.append(index)
    
    return interest

def transpose(data:list) -> list:
    return list(zip(*data))

rows_to_expand = find_rows(data)
cols_to_expand = find_rows(transpose(data))

# find positions of galaxies
universes=[]

for row in range(len(data)):
    for gollum in range(len(data[row])):
        if data[row][gollum] == "#":
            universes.append((gollum, row))
            
pou = {} # pairs of universes

for universe1 in universes:
    for universe2 in universes:
        if universe1 == universe2:
            continue
        else:
            if not (pair:=tuple(sorted((universe1, universe2)))) in pou.keys():
                pou[pair]=0
 
 
def get_distance(universe1:tuple, universe2:tuple, duplicate_factor:int=1) -> int:
    
    add_rows=0
    add_cols=0
    
    for i in range(min(universe1[0], universe2[0]), max(universe1[0], universe2[0])):
        if i in cols_to_expand:
            add_cols+=duplicate_factor
            
    for i in range(min(universe1[1], universe2[1]), max(universe1[1], universe2[1])):
        if i in rows_to_expand:
            add_rows+=duplicate_factor
    
    x = abs(universe1[0]-universe2[0])
    y = abs(universe1[1]-universe2[1])
        
    return x+y+add_rows+add_cols

for key in pou.keys():
    pou[key] = get_distance(*key, 1)

print("Part 1", sum(pou.values()))

for key in pou.keys():
    pou[key] = get_distance(*key, 999999)

print("Part 2", sum(pou.values()))