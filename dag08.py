# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

instr_list=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    instr_list.append([line.split(' ')[0],int(line.split(' ')[1])])
f.close()

visited=set()
cur_instr=0
acc=0
while cur_instr not in visited:
    visited.add(cur_instr)
    if instr_list[cur_instr][0]=='nop':
        cur_instr+=1
        continue
    if instr_list[cur_instr][0]=='jmp':
        cur_instr+=instr_list[cur_instr][1]
        continue
    if instr_list[cur_instr][0]=='acc':
        acc+=instr_list[cur_instr][1]
        cur_instr+=1
        continue
total_p1=acc

finished=False
i=0
while finished==False:
    acc=0
    cur_instr=0
    store=instr_list[i][0]
    visited=set()
    
    if store=='jmp':
        instr_list[i][0]='nop'
    elif store=='nop':
        instr_list[i][0]='jmp'
    else:
        i+=1
        continue

    while cur_instr not in visited:
        if cur_instr>=len(instr_list):
            finished=True
            break
        
        visited.add(cur_instr)
        if instr_list[cur_instr][0]=='nop':
            cur_instr+=1
            continue
        if instr_list[cur_instr][0]=='jmp':
            cur_instr+=instr_list[cur_instr][1]
            continue
        if instr_list[cur_instr][0]=='acc':
            acc+=instr_list[cur_instr][1]
            cur_instr+=1
            continue

    instr_list[i][0]=store
    i+=1


print("Part 1",total_p1)
print("Part 2",acc)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))