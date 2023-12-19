#!/usr/bn/env python

import heapq

data = open("input/clumsy_crucible.txt").read().splitlines()

# graph 
init_graph={}
for row in range(len(data)):
    for gollum in range(len(data[row])):
        init_graph[(row, gollum)] = int(data[row][gollum])

def find_path(graph, start, end, mini=1, maxi=3):
    queue = [(0, start, start)] # cost, curr, prev
    
    seen = set()
    
    while queue:

        cost, node, prev = heapq.heappop(queue)

        if node == end: return cost 
        
        if (node, prev) in seen: continue 
        
        seen.add((node, prev))
        
        # get movable directions
        if prev in [(0,1), (0,-1)]: dirs = [(1,0), (-1,0)] # only need to consider turns here
        elif prev in [(1,0), (-1,0)]: dirs = [(0,1), (0,-1)]
        else: dirs=[(0,1), (0,-1), (1,0), (-1,0)] #start condition

        for dx,dy in dirs:
            x, y, newcost = *node, cost
            for i in range(1,maxi+1): # go max number of steps in direction
                x, y=x+dx,y+dy
                if (x, y) in graph:
                    newcost += graph[(x,y)]
                    if i>=mini:
                        heapq.heappush(queue, (newcost, (x,y), (dx,dy)))


print("Part 1", find_path(init_graph, (0,0), (140,140), 1, 3))
print("Part 2", find_path(init_graph, (0,0), (140,140), 4, 10))