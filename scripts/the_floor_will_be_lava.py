#!/usr/bin/env python

from functools import cache

data = open("input/the_floor_will_be_lava.txt").read().splitlines()

queue = set([(0,0, "E")]) # gollum, row, direction
configs=[queue]

def count_energized(queue, data) -> int:
    visited=set()
    energized=set()
    while queue:
        beam = queue.pop()
        while True: # beam in grid 
            gollum, row, direction = beam

            
            if row < 0 or row >= len(data) or gollum < 0 or gollum >= len(data[0]) or beam in visited:
                break
            
            energized.add((row, gollum)) 
            visited.add(beam)
            
            match direction:
                case "N": # row-1
                    if data[row][gollum] in [".", "|"]:
                        row -= 1
                    elif data[row][gollum] == "/":
                        gollum +=1 
                        direction = "E"
                    elif data[row][gollum] == "\\":
                        gollum -= 1
                        direction = "W"
                    else:
                        # left is current beam, right gets added
                        gollum -= 1
                        direction = "W"
                        queue.add((gollum+1, row, "E"))
                case "S":
                    if data[row][gollum] in [".", "|"]:
                        row += 1
                    elif data[row][gollum] == "/":
                        gollum-=1
                        direction="W"
                    elif data[row][gollum] == "\\":
                        gollum+=1
                        direction = "E"
                    else:
                        # left is current beam, right gets added 
                        gollum -=1 
                        direction = "W"
                        queue.add((gollum+1, row, "E"))
                case "E":
                    if data[row][gollum] in [".", "-"]:
                        gollum+=1
                    elif data[row][gollum] == "/":
                        row-=1
                        direction="N"
                    elif data[row][gollum] == "\\":
                        row+=1
                        direction="S"
                    else:
                        # up is mine, down gets added 
                        row-=1
                        direction="N"
                        queue.add((gollum, row+1, "S"))
                case "W":
                    if data[row][gollum] in [".", "-"]:
                        gollum -=1 
                    elif data[row][gollum] == "/":
                        row+=1
                        direction="S"
                    elif data[row][gollum] == "\\":
                        row-=1
                        direction="N"
                    else:
                        # up is mine, down is added 
                        row-=1 
                        direction="N"
                        queue.add((gollum, row+1, "S"))
                        
            beam = (gollum, row, direction)  
            
        
    return len(energized)
    
print("Part 1", count_energized(set([(0,0,"E")]), data))

def try_configs(data):
    # generate configs
    configs=[]
    for row in range(len(data)):
        configs.append((0, row, "E"))
        configs.append((len(data[0])-1, row, "W"))
    
    for gollum in range(len(data[0])):
        configs.append((gollum, 0, "S"))
        configs.append((gollum, len(data)-1, "N"))
        
    max_ener=[]
    for config in configs:
        print(config)
        max_ener.append(count_energized(set([config]), data))
        
    return max(max_ener)
        
    
# its not the best, but it is honest work (hugging my potato)
# sets are your friends
print("Part 2", try_configs(data))