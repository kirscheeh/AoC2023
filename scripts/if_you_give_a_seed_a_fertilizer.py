#!/usr/bin/env python

def parse_data(path:str="input/if_you_give_a_seed_a_fertilizer.txt") -> tuple[list, dict]:
	data:list = open(path).read().split("\n\n")

	_, numbers = data[0].split(":")
	numbers = [int(x) for x in numbers.split(" ") if not x==""]

	maps = {}

	for line in data[1:]:
		name, *numb = line.split("\n")
		numb = [[int(x) for x in elem.split(" ")] for elem in numb]
		maps[name] = numb
  
	return numbers, maps
 
def iterate_mappings(maps:dict, seed:int, reverse:bool) -> int:
	for _, value in maps.items():
		for elem in value:
			source, dest = elem[1], elem[0]
   
			if reverse:
				source, dest = dest, source
    
			if source <= seed <= source+elem[2]:
				seed = dest + (seed-source)
				break
	return seed
 
def main():
    
	numbers, maps = parse_data()
 
	# Part 1
	min_loc:int = -1
	for seed in numbers:
		seed:int = iterate_mappings(maps, seed, False)
		if seed < min_loc or min_loc == -1:
			min_loc=seed

	print("Part 1", min_loc)

	# Part 2
	ranges:list = [range(numbers[i], numbers[i]+numbers[i+1]) for i in range(0, len(numbers), 2)]
	maps = dict(reversed(list(maps.items())))

	location:int =0

	while True:
		seed = iterate_mappings(maps, location, True)
		
		for r in ranges:
			if seed in r:
				break
		else:
			location+=1
			continue 

		break

	print("Part 2", location)
 
 
if __name__ == "__main__":
    main()