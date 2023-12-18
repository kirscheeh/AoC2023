#!/usr/bin/env python

data = open("input/lavaduct_lagoon.txt").read().splitlines()

data = [tuple(x.split(" ")) for x in data]

curr = (0,0)

border=[curr]

direc = {"0":"R", "1":"D", "2":"L", "3":"U"}

part2 = []
for direction, steps, color in data:
    y, x = curr  #row, gollum
    x, y = int(x), int(y)
    steps = int(steps)

    match direction:
        case "R":
            for step in range(x+1, x+steps+1):
                border.append((y, step))
            curr = (y, step)
        case "L":
            for step in range(x-steps, x):
                border.append((y, step))
            curr = (y, x-steps)
        case "D":
            for step in range(y+1, y+steps+1):
                border.append((step, x))
            curr = (step, x)
        case "U":
            for step in range(y-steps, y):
                border.append((step, x))
            curr = (y-steps, x)
           
    part2.append((direc[color[-2]], int(color[2:-2], 16)))
            
# build grid
maxrow = max([x for x, y in border])
maxgol = max([y for x, y in border])
minrow = min([x for x, y in border])
mingol = min([y for x, y in border])
rowshift=0
golshift=0

if minrow < 0:
    rowshift=abs(minrow)
if mingol < 0:
    golshift=abs(mingol)

border = list(set(border))
border = [(row+rowshift, gol+golshift) for row, gol in border]

shift=2
grid=[["x" for gol in range(min(0, mingol-shift),maxgol+shift+1)] for row in range(min(0, minrow-shift), maxrow+shift+1)]

for row, gollum in border:
    if (row+1, gollum) in border and (row, gollum+1) in border:
        grid[row+shift][gollum+shift] = "F"
    elif (row-1, gollum) in border and (row, gollum+1) in border:
        grid[row+shift][gollum+shift] = "L"
    elif (row+1, gollum) in border and (row, gollum-1) in border:
        grid[row+shift][gollum+shift] = "7"
    elif (row-1, gollum) in border and (row, gollum-1) in border:
        grid[row+shift][gollum+shift] = "J"
    elif (row-1, gollum) in border and (row+1, gollum) in border:
        grid[row+shift][gollum+shift] = "|"
    elif (row, gollum-1) in border and (row, gollum+1) in border:
        grid[row+shift][gollum+shift] = "-"
    else:
        print("WTF")
        
border = [(row+shift, gol+shift) for row, gol in border]

#P art 1
inside=0
for row, line in enumerate(grid):
    for gollum, char in enumerate(line):
        if (row, gollum) in border: # do not check for element in pipe
            continue 

        inside += sum([line[:gollum].count("J"), line[:gollum].count("|"), line[:gollum].count("L")]) % 2 == 1 # uneven counts of my elements means my dot is inside
        
print("Part 1", inside+len(set(border)))



print(part2)
curr=(0,0)
border=[curr]
border_length=0
for direction, steps in part2:
    y, x = curr  #row, gollum
    border_length+=steps
    match direction:
        case "R":
            for step in range(x+1, x+steps+1):
                pass#border_length+=1
            curr = (y, step)
        case "L":
            for step in range(x-steps, x):
                border_length+=1
            curr = (y, x-steps)
        case "D":
            for step in range(y+1, y+steps+1):
                pass#border_length+=1
            curr = (step, x)
        case "U":
            for step in range(y-steps, y):
                pass#border_length+=1
            curr = (y-steps, x)
    border.append(curr)

from itertools import tee

def pairwise(iterable):
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)

def shoelace(vertices):
	area = 0
	for (r1, c1), (r2, c2) in pairwise(vertices):
		area += (r2 + r1) * (c2 - c1)

	return abs(area) // 2

def solve(vertices, perimeter):
	area = shoelace(vertices)
	return int(area - perimeter / 2 + 1) + perimeter

border = border[:-1]#[::-1]

print(solve(border, border_length))