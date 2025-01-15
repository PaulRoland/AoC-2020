# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
start_time = time.time_ns()

f = open("input.txt", "r")
numbers=set()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    a=int(line)
    numbers.add(a)
    if 2020-a in numbers:
        p1=a*(2020-a)
    for b in numbers:
        if 2020-a-b in numbers:
            p2=a*b*(2020-a-b)
f.close()

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))