# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def analyse_group(entries):
    unions=set(list(entries[0]))
    inters=set(list(entries[0]))
    for entry in entries[1:]:
        unions=unions.union(set(list(entry)))
        inters=inters.intersection(set(list(entry)))
    return [len(unions),len(inters)]


f = open("input.txt", "r")
groups=list()
entries=list()
for i,line in enumerate(f):
    if line=='\n':
        groups.append(entries)
        entries=list()
        continue
    entries.append(line.replace('\n',''))
f.close()
groups.append(entries)

total_p1=0
total_p2=0
for entries in groups:
    [p1,p2]=analyse_group(entries)
    total_p1+=p1
    total_p2+=p2

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))