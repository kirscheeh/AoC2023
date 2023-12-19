#!/usr/bin/env python

from functools import cache

data = open("input/parabolic_reflector_dish.txt").read().splitlines()

rocks:list = []
rolls:list = []
frees:list = []

for rowindx, row in enumerate(data):
    for gollumindx, gollum in enumerate(row):
        match gollum:
            case "#":
                rocks.append((rowindx, gollumindx))
            case "O":
                rolls.append((rowindx, gollumindx))
                  
                        
def north(rocks, rolls):
    rolls.sort()

    occupied:list = []
    for row, gollum in rolls:

        while True: # which other condition?
            if not (row-1, gollum) in occupied+rocks and row-1 >=0:
                row -=1
            else:
                break
        occupied.append((row, gollum))
    return occupied

def south(rocks, rolls, length:int):
    rolls = sorted(rolls, reverse=True)
    
    occupied:list = []
    for row, gollum in rolls:

        while True: # which other condition?
            if not (row+1, gollum) in occupied+rocks and row+1 < length:
                row +=1
            else:
                break
        occupied.append((row, gollum))
    return occupied

def west(rocks, rolls):
    rolls = sorted(rolls, key=lambda x:x[1])
    occupied:list = []
    for row, gollum in rolls:

        while True: # which other condition?
            if not (row, gollum-1) in occupied+rocks and gollum-1 >= 0:
                gollum -=1
            else:
                break
        occupied.append((row, gollum))
    return occupied

def east(rocks, rolls, width:int):
    rolls = sorted(rolls, key=lambda x:x[1], reverse=True)
    occupied:list = []
    for row, gollum in rolls:

        while True: # which other condition?
            if not (row, gollum+1) in occupied+rocks and gollum+1 < width:
                gollum +=1
            else:
                break
        occupied.append((row, gollum))
        
    return occupied
        
def calc_total_load(positions:list, length:int) -> int:
    result=0
    for row, gollum in positions:
        result += (length-row)
    return result
    
cache_config={}
cycle_found=False

cycles = 1_000_000_000
cycle_index=0


while cycle_index < cycles:    
    
    rolls = north(rocks, rolls)
    
    if cycle_index == 0:
        print("Part 1", calc_total_load(rolls, len(data)))
    
    rolls = west(rocks, rolls)
    rolls = south(rocks, rolls, len(data))
    rolls = east(rocks, rolls, len(data[0]))
    
    config = tuple(sorted(rolls))
    
    cycle_index+=1
    
    if not cycle_found and (cycle_found:= config in cache_config.keys()): #find cycle
        length_cycle = cycle_index - cache_config[config] 
        cycle_index += length_cycle * ((cycles - cycle_index) // length_cycle) # skip to latest moment before the billion
    else:
        cache_config[config] = cycle_index

print("Part 2", calc_total_load(rolls, len(data)))
    
