#!/usr/bin/env python

import re
workflowlist, partslist = open("input/aplenty.txt").read().split("\n\n")

print(partslist)

workflowlist = workflowlist.splitlines()

workflows:dict = {}

for workflow in workflowlist:
    workflow = workflow.replace("{", ",").replace("}", ",")
    name, *workflow, fallback = workflow.split(",")[:-1]

    workflows[name] = {}
    for condition in workflow:
        condition, consequence = condition.split(":")
        category, sign, *value = condition

        workflows[name][condition] = (category, sign, int("".join(value)), consequence)

    workflows[name]["fb"] = (None, None, None, fallback)
print(workflows)

parts = []
for part in partslist.splitlines():
    partdic = {}
    for match in re.finditer("[xmas]\=[0-9]{1,}", part):
        category, value = match.group().split("=")
        partdic[category] = int(value)

    parts.append(partdic)

parts = tuple(parts)
curr = "in"
print(parts)

def find_new_workflow(workflow, part) -> str:
    for name, (category, sign, value, consequence) in workflow.items():
        if name == "fb":
            continue
        if eval(str(part[category])+sign+str(value)):
            return consequence
    return workflow["fb"][3]

accepted=[]
rejected=[]
for part in parts:

    print(part)
    while not curr in "RA":
        curr = find_new_workflow(workflows[curr], part)
        print(curr)


    if curr == "A":
        print(part)
        accepted.append(sum(part.values()))

    curr = "in"

print(sum(accepted))
