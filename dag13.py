# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import sympy as sp
import itertools as it
import math


f = open("input.txt", "r")
start=int(f.readline().replace('\n',''))
busses=list()
counter=0
for line in f:
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for i,d in enumerate(line.split(',')):
        if d=='x':
            continue
        busses.append([i,int(d),counter])
        counter+=1
f.close()

dt1,bus1,i1=busses[0]

best=bus1*(start//bus1+1)-start
best_ID=bus1

#First options for n are 0+1*n
a=0
b=1

for [dt2,bus2,i2] in busses[1:]:
     n has a bigger step and offset after each new bus iteration
    # Example: 17n1 = 13n2 - 2
    # 17n1+2=13n2
    # Find options for n1:
    # n1 = 6 + 13n (6 found using brute force, 13 from equation)
    # 17n1 = 19n3-2
    # 17n1+2=19n3
    # n1 = 6+13n
    # 102+13*17n+2=19n3 
    # Find options for n
    # n = 15 + 19nn (15 found using brute force, 19 from equation)
    # n1 = 6+13n
    # n1 = 6+13*(15+19nn) = 201 + 247nn
    # First solution, nn=0 is timestamp 201*17
    # Repeat for all buslines
    
    i=0
    while True:
        i+=1
        
        if (bus1*(a+b*i)+dt2) % bus2==0:
            break

    a=a+b*i
    b=b*bus2
    bustime=bus2*(start//bus2+1)
    if bustime-start<best:
        best=bustime-start
        best_ID=bus2
        
print("Part 1",best*best_ID)
print("Part 2",a*bus1)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
