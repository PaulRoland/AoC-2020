# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
grid=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    grid.append(line)
f.close()

slope=3
p1=0
slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]
slope_trees=list()
for slope in slopes:
    trees=0
    i=0
    while i*slope[1]<len(grid):
        line=grid[i*slope[1]]
        if line[i*slope[0]%len(line)]=='#':
            trees+=1
        i+=1
    print(trees)
    slope_trees.append(trees)
    


print("Part 1",slope_trees[1])
print("Part 2",slope_trees[0]*slope_trees[1]*slope_trees[2]*slope_trees[3]*slope_trees[4])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))