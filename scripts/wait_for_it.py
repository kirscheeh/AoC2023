#!/usr/bin/env python

import re
import math

def parse_input(path:str="input/wait_for_it.txt", one_number:bool=False):
    data:list = open(path).read().splitlines()

    # Part 1
    time:list = list(map(int, re.findall("[0-9]{1,}", data[0])))
    dist:list = list(map(int, re.findall("[0-9]{1,}", data[1])))

    # Part 2
    if one_number:
        time:list = [int("".join(re.findall("[0-9]{1,}", data[0])))]
        dist:list = [int("".join(re.findall("[0-9]{1,}", data[1])))]
        
    return time, dist

def get_winnings(time:list, dist:list) -> int:

    ways:list=[]
    for t, d in zip(time, dist):
        certain_wins:int=0
        for button_pressed in range(1, t):
            traveled:int = button_pressed*(t-button_pressed) 
            if traveled > d:
                certain_wins+=1
        ways.append(certain_wins)
        
    return math.prod(ways)

def main():
    time, dist = parse_input()
    print("Part 1", get_winnings(time, dist))
    
    time, dist = parse_input(one_number=True)    
    print("Part 2", get_winnings(time, dist))
    
if __name__ == "__main__":
    main()