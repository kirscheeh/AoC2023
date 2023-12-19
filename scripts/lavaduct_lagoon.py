#!/usr/bin/env python

# initially adapted day 10 for part 1, but after getting an idea for part two, switched completely to shoelace and pick's theorem

data = open("input/lavaduct_lagoon.txt").read().splitlines()

data = [tuple(x.split(" ")) for x in data]
part1 = [(x[0], int(x[1])) for x in data]

directions = {"0":"R", "1":"D", "2":"L", "3":"U"}
part2 = [(directions[x[2][-2]], int(x[2][2:-2], 16)) for x in data]

def get_borders(data:tuple[str, tuple[int, int]]) -> list[int]:
    curr = (0,0)
    
    points:list = []
    length:int = 0
    for direction, steps in data:
        y, x = curr  #row, gollum
        length+=steps
        
        match direction:
            case "R":
                curr = (y, x+steps)
            case "L":
                curr = (y, x-steps)
            case "D":
                curr = (steps+y, x)
            case "U":
                curr = (y-steps, x)
                
        points.append(curr)
        
    return tuple(points), length

def shoelace(polygonBoundary, absoluteValue = True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2.)
    else:
        return sum(l) / 2.

def picks(area, points) -> int:
    return area - points/2 + 1

p1, length = get_borders(part1)
p1 = p1[::-1]

area=shoelace(p1)
print("Part 1", int(picks(area, length)+length))

p2, length = get_borders(part2)
p2 = p2[::-1]

area=shoelace(p2)
print("Part 2", int(picks(area, length)+length))