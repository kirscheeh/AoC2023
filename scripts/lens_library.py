#!/usr/bin/env python

init = open("input/lens_library.txt").read().strip().split(",")
print(init)
def hashit(tohash:str, currval:int =0) -> int:
    tohash = ord(tohash)

    currval += tohash
    currval *= 17
    currval %= 256
    
    return currval


lensboxes={}
sum_init=0
for elem in init:
    currval=0
    if "=" in elem:
        tohash = elem[:-2]
    else:
        tohash = elem[:-1]
        
    for schtring in tohash:
        currval = hashit(schtring, currval)
        
    if not currval in lensboxes.keys():
        lensboxes[currval] = []
        
    if "=" in elem:
        for index, (type, thing) in enumerate(lensboxes[currval]):
            if type == tohash:
                lensboxes[currval][index] = (tohash, int(elem[-1]))
                break
        else:
            lensboxes[currval].append((tohash, int(elem[-1])))
    else:
        if len(lensboxes[currval]) == 0:
            pass
        else:
            to_remove=None
            for type, thing in lensboxes[currval]:
                if type == tohash:
                    to_remove = (type, thing)
            if to_remove:
                lensboxes[currval].remove(to_remove)
            
    print(elem, currval)
    sum_init += currval
    
#print("Part 1", sum_init)
adding=0
for key, value in lensboxes.items():
    for index, (a, b) in enumerate(value):
        adding += (key+1)*b*(index+1)
print(adding)