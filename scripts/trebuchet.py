#!/usr/bin/env python

import re

def read_calibration_document(instructions:list[str], new_knowledge:bool = False) -> list[int]:
	"""
	Try to decipher the calibration values.
 
	As they're [the Elves] making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf  who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
  
	Args:
		instructions (list[str]): Each line originally contained a specific calibration value that the Elves now need to recover. 
		new_knowledge (bool, optional):	It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight,  and nine also count as valid "digits". Defaults to False.

	Returns:
		list[int]: List of deciphered calibration values. The calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
	""" 
 
	spelledOutLetters:dict[str,str] = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}	
 
	calibration_scores:list[int] = []
 
	for instr in instructions:
		digits:list[str]
		
		if new_knowledge:
			digits = re.findall("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", instr)
			digits = [spelledOutLetters[dig] if dig in spelledOutLetters.keys() else dig for dig in digits]
		else:
			digits = re.findall("[1-9]", instr)
		
		calibration_scores.append(int(digits[0]+digits[-1]))
	
	return calibration_scores

def main():
    """
    Advent of Code 2023 --- Day 1: Trebuchet?! ---
    
    You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
    
    As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
    
    """
    encrypted_calibration_scores:list[str] = open("input/trebuchet.txt").read().splitlines()
    
    print("Part 1:", sum(read_calibration_document(encrypted_calibration_scores)))
    print("Part 2:", sum(read_calibration_document(encrypted_calibration_scores, True)))

if __name__ == "__main__":
	main()