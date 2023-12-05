#!/usr/bin/env python

import pandas as pd

data = open("input/if_you_give_a_seed_a_fertilizer.txt").read().split("\n\n")

seeds, numbers = data[0].split(":")
numbers = [int(x) for x in numbers.split(" ") if not x==""]

maps = {}

for line in data[1:]:
	name, *numb = line.split("\n")
	numb = [[int(x) for x in elem.split(" ")] for elem in numb]
	maps[name] = numb

print(numbers)
checker=-1

for i in range(0, len(numbers), 2):
	for seed in [a for a in range(numbers[i], numbers[i]+numbers[i+1])]:
		for key, value in maps.items():
			for elem in value:
				if elem[1] <= seed <= elem[1]+elem[2]:
					seed = elem[0] + (seed-elem[1])
					break
		if checker == -1:
			checker = seed
		if seed < checker:
			checker = seed
		print(checker)
	#checker.append(seed)
print(checker)
print("Part 2", checker)
