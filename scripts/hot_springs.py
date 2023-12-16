#!/usr/bin/env python

import re
from itertools import combinations

data = open("input/hot_springs.txt").read().splitlines()

for line in data:
    formation, counts = line.split(" ")
    
    # add dummy end .
    formation += "."
    
    damaged = re.findall("([\?#]{1,}).", formation)
    
    input()
    
    
    
# group needs to end with #.

