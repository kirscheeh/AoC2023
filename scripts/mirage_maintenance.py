#!/usr/bin/env python


def parse_input(path:str="input/mirage_maintenance.txt") -> list[list[int]]:
    data = open(path).read().splitlines()
    return [[int(y) for y in x.split(" ")] for x in data]


def get_history(sequences:list, forward:bool=True) -> list[int]:
    if forward:
        elem_index:int=-1
    else:
        elem_index:int=0

    history:list=[]
    for seq in sequences: 
        digits:list=[seq[elem_index]]
        while not seq.count(0) == len(seq):
            new_seq:list=[]
            for index in range(0,len(seq)-1):
                new_seq.append(seq[index+1]-seq[index]) 
            seq=new_seq    
            digits.append(seq[elem_index])
        
        if not forward:
            digits.reverse()

        value:int=0
        for elem in digits:
            if forward:
                value += elem
            else:
                value = elem-value
        history.append(value)

    return history

def main():
    sequences =parse_input()
    print("Part 1", sum(get_history(sequences)))
    print("Part 2", sum(get_history(sequences, False)))


if __name__ == "__main__":
    main()