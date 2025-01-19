# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


f = open("input.txt", "r")

direc=[[0,1],[1,0],[0,-1],[-1,0]]
wayp=[-1,10]
dir_n=0
x=0
y=0
x2=0
y2=0

for i,line in enumerate(f):
    line=line.replace('\n','')
    ltr=line[0]
    n=int(line[1:])
    if ltr=='N':
        y-=n
        wayp[0]-=n
    if ltr=='E':
        x+=n
        wayp[1]+=n
    if ltr=='S':
        y+=n
        wayp[0]+=n
    if ltr=='W':
        x-=n
        wayp[1]-=n
    if ltr=='F':
        y+=direc[dir_n][0]*n
        x+=direc[dir_n][1]*n
        y2+=wayp[0]*n
        x2+=wayp[1]*n 
    if ltr=='L':
        dir_n=(dir_n-n//90)%4
        for _ in range(0,n//90):
            tmp=wayp[0]
            wayp[0]=-wayp[1]
            wayp[1]=tmp
            
    if ltr=='R':
        dir_n=(dir_n+n//90)%4
        for _ in range(0,n//90):
            tmp=wayp[0]
            wayp[0]=wayp[1]
            wayp[1]=-tmp
f.close()

total_p1=abs(x)+abs(y)
total_p2=abs(x2)+abs(y2)
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))