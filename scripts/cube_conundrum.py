#!/usr/bin/env python3

import re

def process_data(path:str="input/cube_conundrum.txt") -> dict[int, list[list[int]]]:
    """
        Given a line for each game, the information will be parsed into a dictionary with the game number as key and three lists containing the values for red, green and blue cubes of the different rounds.
    """

    data:list[str] = open(path).read().splitlines()

    results:dict[int, list] = {}

    for line in data:
        game = int(re.findall("Game ([0-9]{1,3})", line)[0])

        blues:list[int] = list(map(int, re.findall("([0-9]{1,}) blue", line)))
        reds:list[int] = list(map(int, re.findall("([0-9]{1,}) red", line)))
        greens:list[int] = list(map(int, re.findall("([0-9]{1,}) green", line)))

        results[game] = [blues, reds, greens]

    return results


def find_possible_games(data:dict[int, list[list[int]]], red:int=12, green:int = 13, blue:int =14) -> list[int]:
    possible_games:list[int] = []

    for game, values in data.items():
        if max(values[0]) > blue or max(values[1]) > red or max(values[2]) > green:
            continue

        possible_games.append(game)

    return possible_games

def find_minimum_cubes(data:dict[int, list[list[int]]]) -> list[int]:
    powers:list[int] = []

    for _, (blues, reds, greens) in data.items():
        powers.append(max(blues)*max(reds)*max(greens))

    return powers

def main():
    game_bag = process_data()
    print("Part 1:", sum(find_possible_games(game_bag)))
    print("Part 2:", sum(find_minimum_cubes(game_bag)))


if __name__ == "__main__":
    main()
