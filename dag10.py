# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def recurse_adapters(jolts,start,end):
    if start in mem:
        return mem[start]
    if start==end:
        return 1
    total=0
    for delta in range(1,4):
        if start+delta in jolts:
            total+=recurse_adapters(jolts,start+delta,end)
    mem[start]=total
    return total
    

jolts=[int(d.replace('\n','')) for d in open("input.txt", "r").readlines()]
jolts.append(0)
jolts.append(max(jolts)+3)
jolts.sort() 

diff_list=[0,0,0,0]
for a,b in zip(jolts,jolts[1:]):
    diff=b-a
    diff_list[diff]+=1
    
total_p1=diff_list[1]*(diff_list[3])

mem=dict()
total_p2=recurse_adapters(jolts,0,max(jolts))

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))