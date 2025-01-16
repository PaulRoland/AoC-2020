# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
ids=list()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    line2=line.replace('B','1').replace('F','0').replace('R','1').replace('L','0')
    ID=int(line2[0:7],2)*8+int(line2[7:],2)
    ids.append(ID)
f.close()

ids.sort()
for id1,id2 in zip(ids,ids[1:]):
    if id1+1!=id2:
        p2=id1+1
                           

print("Part 1",max(ids))
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))