# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
import time
start_time = time.time_ns()

def crab_cup(cups,moves,c_min,c_max,cur_cup):
    for i in range(0,moves):
        c1=cups[cur_cup]
        c2=cups[c1]
        c3=cups[c2]
        
        dest=cur_cup-1
        if dest<c_min:
            dest=c_max
        while dest in [c1,c2,c3]:
            dest-=1
            if dest<c_min:
                dest=c_max
        
        cups[cur_cup]=cups[c3]
        tmp=cups[dest]
        cups[dest]=c1
        cups[c3]=tmp
        
        cur_cup=cups[cur_cup]
    return cups


f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
f.close()

cups=dict()
start_nums=[int(d) for d in list(line)]
for a,b in zip(start_nums,start_nums[1:]):
    cups.update({a:b})
cups.update({start_nums[-1]:start_nums[0]})


cups=crab_cup(cups,100,1,9,start_nums[0])
start=1
counts=1
string='' 
while counts<len(cups):
     start=cups[start]
     string+=str(start)
     counts+=1
total_p1=string

start_nums=start_nums+list(range(max(start_nums)+1,1000001))
cups=dict()
for a,b in zip(start_nums,start_nums[1:]):
    cups.update({a:b})
cups.update({start_nums[-1]:start_nums[0]})
cups=crab_cup(cups,10000000,1,1000000,start_nums[0])
total_p2=cups[1]*cups[cups[1]]

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))