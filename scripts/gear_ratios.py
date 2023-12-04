#!/usr/bin/env python3

import re
import sys

def process_data(path:str="input/gear_ratios.txt", only_gear:bool=False) -> tuple[list[set[int, int]], list[set[str, int, int]]]:
    data = open(path).read().splitlines()
    
    special_signs:list[set(int, int)] = []
    numbers:list[set(str, int, int)] = []
    for row, gollum in enumerate(data):
        # get all special characters or only gears (*)
        
        if only_gear:
            pattern="\*"
        else:
            pattern="[^0-9\.]"
            
        for sign in re.finditer(pattern, gollum):
            special_signs.append((row, sign.start()))
            
        # get all numbers of a line
        for num in re.finditer("[0-9]{1,}", gollum):
            numbers.append((num.group(), row, num.start()))
            
    return special_signs, numbers
     
def get_part_numbers(spec:list, numbers:list) -> dict[set[int, int]:int]:
    
    results={pos:[] for pos in spec}
    
    for num, row, gollum in numbers:
        gollum_pos = [x for x in range(gollum-1, gollum+len(num)+1)]
        
        for gol in gollum_pos:
            if (row, gol) in spec:
                results[(row, gol)].append(int(num))
            elif (row-1, gol) in spec:
                results[(row-1, gol)].append(int(num))
            elif (row+1, gol) in spec:
                results[(row+1, gol)].append(int(num))
                
    return results
                
def main():
    # Part 1
    special_signs, numbers = process_data()
    
    tmp = get_part_numbers(special_signs, numbers)
    result = sum([sum(x) for x in tmp.values()])
    print("Part 1", result)
    
    # Part 2
    special_signs, numbers = process_data(only_gear=True)
    
    tmp = get_part_numbers(special_signs, numbers)
    result = sum([x[0]*x[1] for x in tmp.values() if len(x) == 2])
    print("Part 2", result)
   
   
if __name__ == "__main__":
    main()