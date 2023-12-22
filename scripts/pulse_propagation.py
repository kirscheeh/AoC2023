#!/usr/bin/env python

data = open("input/pulse_propagation.txt").read().splitlines()

configuration={}

destination_status={}

inverters={}

for line in data:
    name, modules = line.split(" -> ")
    
    if name == "broadcaster":
        configuration["broadcaster"] = tuple(modules.split(", "))
        continue
    
    modtype = name[0]
    modname = name[1:]
    configuration[modname] = tuple(modules.split(", "))
    
    destination_status[modname] = (modtype, 0) # 0 off/low, 1 on/high
    
    if modtype == "&":
        inverters[modname] = []
    
def sent_pulses(impulse, destination):
    global destination_status, configuration
    print(destination_status[destination])
    match (destination_status[destination], impulse):
        case (("%", 0), 1): # swith is off and receives high impulse --> ignore
            pass
        case (("%", 0), 0): # switch is off and receives low impulse -> on and high impulse
            impulse=1
            destination_status[destination] = ("%", 1)
        case (("%", 1), 1): # switch us on and recieves high impulse -> off and sents low impulse
            impulse=0
            destination_status[destination] = ("%", 0)
        case (("%", 1), 0): # switch is on and receives low impulse -> off and sends high impulse
            impulse=0
            destination_status[destination] = ("%", 1)
        case (("%", 1), 1): # logical and
            impulse=0
        case (("%", 0), 0) | (("%", 1), 0) | (("%", 0), 1): 
            impulse=1
    return impulse
            
        

    
print(sent_pulses(0, "a"))