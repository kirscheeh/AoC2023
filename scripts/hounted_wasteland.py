#!/usr/bin/env python

import itertools
import math
import sys 

def parse_input(path:str="input/hounted_wasteland.txt") -> tuple[dict, list]:
    data = open(path).read()

    instruction, maps = data.split("\n\n")
    maps = maps.splitlines()
    tree = {x.split("=")[0].strip():(x.split("(")[1][:3].strip(), x.split(",")[1][:4].strip()) for x in maps}

    instructions = [*instruction.replace("L", "0").replace("R", "1")]
    
    return tree, instructions


def find_end(tree:dict, instructions:list, node="AAA") -> int:
    counter=0
    while not node.endswith("Z"):
        for move in instructions:
            node = tree[node][int(move)]
            counter+=1
    return counter

      
def main():
    tree, instructions = parse_input()
    print("Part 1", find_end(tree, instructions))
    
    node_A = [x for x in tree.keys() if x.endswith("A")]
    steps=[]
    for node in node_A:
        steps.append(find_end(tree, instructions, node))
    print("Part 2", math.lcm(*steps))
    
    
if __name__ == "__main__":
    main()