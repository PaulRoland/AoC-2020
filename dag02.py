# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
p1=0
p2=0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [a,b]=[int(d) for d in line.split(' ')[0].split('-')]
    s=line.split(' ')[1].replace(':','')
    pw=line.split(' ')[2]
    n=pw.count(s)
    
    if n>=a and n<=b:
        p1+=1
    
    if pw[a-1]==s and pw[b-1]!=s:
        p2+=1
    elif pw[a-1]!=s and pw[b-1]==s:
        p2+=1
        
        
    
f.close()

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))