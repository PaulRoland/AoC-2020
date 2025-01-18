# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
start_time = time.time_ns()


def sum_previous(preamble,numbers):
    for i,n in enumerate(numbers[preamble:]):
        valid=False
        for j in range(0,preamble):
            if n-numbers[i+j] in numbers[i+j:i+preamble+j]:
                valid=True
                break
            
        if valid==False:        
            return n   

def contiguous_set(total,numbers):
    for n in range(3,len(numbers)):
        for i in range(0,len(numbers)-n):
            if sum(numbers[i:i+n])==total:
                   return min(numbers[i:i+n])+max(numbers[i:i+n])    
    

numbers=[int(d.replace('\n','')) for d in open("input.txt", "r").readlines()]
total_p1=sum_previous(25,numbers)
total_p2=contiguous_set(total_p1,numbers)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))