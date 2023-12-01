#!/usr/bin/env python

import re
from word2number import w2n

data = open("input/day01.txt").read().splitlines()

val=0
for line in data:
    digits = re.findall("[0-9]", line)
    val += int(digits[0]+digits[-1])
    
print("Part 1", val)

val=0
for line in data:
	finds = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
	
	first = finds[0]
	last  = finds[-1]
 
	first = str(w2n.word_to_num(first))
	last = str(w2n.word_to_num(last))
	
	val += int(first+last)

print("Part 2", val)

