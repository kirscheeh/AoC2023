#!/usr/bin/env python

data = open("input/pipe_maze.txt").read().splitlines()

matrix = [[False for x in row] for row in data]
for row, line in enumerate(data):
    for gollum, char in enumerate(line):
        if char == "S":
            start_pos = (row, gollum)

# get type of S
type_s = "7"

# there can only be one path, right? So i need to find it
# preferably goinf up and right, left, down
pos = start_pos
visited=[]

while not visited.count(start_pos) == 2: # the recusrive way just did not work
    row, gollum = pos
    if data[row][gollum] == "-":
        if (row, gollum+1) in visited:
            pos = (row, gollum-1)
            visited.append((row, gollum))
        else:
            pos = (row, gollum+1)
            visited.append((row, gollum))
    elif data[row][gollum] == "|":
        if (row-1, gollum) in visited:
            pos = (row+1, gollum)
            visited.append((row, gollum))
        else:
            pos = (row-1, gollum)
            visited.append((row, gollum))
    elif data[row][gollum] in ["F"]:

        if (row+1, gollum) in visited:
            pos = (row, gollum+1)
            visited.append((row, gollum))
        else:
            pos = (row+1, gollum)
            visited.append((row, gollum))

    elif data[row][gollum] in  ["7", "S"]:
        if (row+1, gollum) in visited: # i do not know why it has the be this way around, if i first check for (row, gollum-1) I end in an endless loop
            pos = (row, gollum-1)
            visited.append((row, gollum))
        else:
            pos = (row+1, gollum)
            visited.append((row, gollum))
    
    elif data[row][gollum] == "J":
        if (row-1, gollum) in visited:
            pos = (row, gollum-1)
            visited.append((row, gollum))
        else:
            pos = (row-1, gollum)
            visited.append((row, gollum))
        
    elif data[row][gollum] == "L":
        if (row, gollum+1) in visited:
            pos = (row-1, gollum)
            visited.append((row, gollum))
        else:
            pos =(row, gollum+1)
            visited.append((row, gollum))
    else:
        print(data[row][gollum], visited, row, gollum) # this shouls never happen
        break

print((len(visited)-1)/2)

# Part 2
## Vector Shape Rasterization; count times you are crossing the border of your pipes; either going | L J or | F 7
# count | L J

data = [[x for x in line] for line in data]
for row, line in enumerate(data): # so that I actually only count loop pipes and not all pipes
    for gollum, char in enumerate(line):
        if (row, gollum) in visited:
            if data[row][gollum] == "J":
                data[row][gollum] ="X"
            if data[row][gollum] == "L":
                data[row][gollum] ="Y"
            if data[row][gollum] == "|":
                data[row][gollum] ="Z"

inside=0
for row, line in enumerate(data):
    for gollum, char in enumerate(line):
        if (row, gollum) in visited: # do not check for element in pipe
            continue 

        inside += sum([line[:gollum].count("X"), line[:gollum].count("Y"), line[:gollum ].count("Z")]) % 2 == 1 # uneven counts of my elements means my dot is inside

print(inside)
