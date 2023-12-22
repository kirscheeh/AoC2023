#!/usr/bin/env python

data = open("input/step_counter.txt").read().splitlines()

rocks=[]
plots=[]
start=None

# find start pos 
for row, line in enumerate(data):
    for gollum, character in enumerate(line):
        match data[row][gollum]:
            case "S":
                start=(row, gollum)
                plots.append((row, gollum))
            case ".":
                plots.append((row, gollum))
            case "#":
                rocks.append((row, gollum))
                
new_pos = [start]

for i in range(64):
    queue = new_pos
    new_pos = set()
    for row, gollum in queue:
        # up
        if (row-1, gollum) in plots:
            new_pos.add((row-1, gollum)) 
            
        # left
        if (row, gollum-1) in plots:
            new_pos.add((row, gollum-1))
            
        # down
        if (row+1, gollum) in plots:
            new_pos.add((row+1, gollum))
            
        # right
        if (row, gollum+1) in plots:
            new_pos.add((row, gollum+1))
            
print("Part 1", len(new_pos))
                
