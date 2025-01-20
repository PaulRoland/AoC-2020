# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    numbers=[int(d) for d in line.split(',')]
    
f.close()


i=0
last_call=dict()

while i<30000000:
    if i==2020:
        total_p1=call
    if i<len(numbers):
        call=numbers[i]    
    
    if i>=len(numbers):
        if first==True:
            call=0
        else:
            call=i-last_call[call][-2]
 
    if call in last_call:
        first=False
        last_call[call].append(i+1)
    else:
        first=True
        last_call.update({call:[i+1]})
    i+=1
    



print("Part 1",total_p1)
print("Part 2",call)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))