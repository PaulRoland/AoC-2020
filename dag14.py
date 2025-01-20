# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

line_data=list()
data=list()
f = open("input.txt", "r")
length=36

for i,line in enumerate(f):
    line=line.replace('\n','')
    if 'mask' in line:
        data.append(line_data)
        line_data=list()
        line_data.append(line[7:])
    else:
        line_data.append([int(d) for d in re.findall('\d+',line)])

    
f.close()
data.append(line_data)
data=data[1:]
#Part 1
mem=dict()
for dataset in data:
    mask = dataset[0]
    for [mem_loc,value] in dataset[1:]:
        bin_string=bin(value)[2:].zfill(length)
        
        result=''
        for m,b in zip(mask,bin_string):
            if m=='X':
                result+=b
            else:
                result+=m
        mem.update({mem_loc:int(result,2)})
                    
total_p1=0
for key in mem:
    total_p1+=mem[key]

#Part 2
mem=dict()
for dataset in data:
    mask = dataset[0]
    for [mem_loc,value] in dataset[1:]:

        bin_string=bin(mem_loc)[2:].zfill(length)

        results=list()
        results.append('')
        
        for m,b in zip(mask,bin_string):
            if m=='0':
                for i,result in enumerate(results):
                    results[i]=result+b
            elif m=='1':
                for i,result in enumerate(results):
                    results[i]=result+'1'
            elif m=='X':
                new_results=list()
                for result in results:
                    new_results.append(result+'0')            
                    new_results.append(result+'1')
                results=list(new_results)
                
        for result in results:
            mem.update({int(result,2):value})          
total_p2=0
for key in mem:
    total_p2+=mem[key]    
    
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))