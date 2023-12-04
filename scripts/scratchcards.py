#!/usr/bin/env python

import re
import sys

def get_cards(path:str="input/scratchcards.txt") -> dict:
    data = open(path).read().splitlines()

    values:dict[int, int] = {}

    for line in data:
        cards, numbers = line.split(":")
        
        card:str = re.findall("[0-9]{1,}", cards)[0]
        
        winner, your_deck = numbers.split("|")
        
        winner:list = set([x for x in winner.strip().split(" ") if not x ==""])
        your_deck:list = set([x for x in your_deck.strip().split(" ") if not x ==""])
        
        overlaps:int = len(winner.intersection(your_deck))
        values[int(card)] = overlaps
        
    return values
        
def get_winning_numbers(values:dict) -> int:
    points:int = 0
    
    for _, point in values.items():
        points += 2**(point-1) if point > 0 else 0
        
    return points

def get_number_cards(values:dict) -> int:
    queue:list = [(key, value) for key, value in values.items()]
    
    cards:int = 0
    
    while queue:
        card, val = queue.pop()
    
        for i in range(card+1, card+val+1):
            queue.append((i, values[i]))

        cards+=1
    
    return cards
        
def main(): 
    data = get_cards()
    print("Part 1", get_winning_numbers(data))
    print("Part 2", get_number_cards(data))

if __name__ == "__main__":
    main()