# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def perf_cycle_3d(cube_active,n,dims):
    new_cube_active=set()

    for z in range(-n,dims[0]+n+1):
        for y in range(-n,dims[1]+n+1):
            for x in range(-n,dims[2]+n+1):
                
                nbrs=0
                for dz in range(-1,2):
                    for dy in range(-1,2):
                        for dx in range(-1,2):
                            if dz==0 and dy==0 and dx==0:
                                continue
                            key=str(z+dz)+','+str(y+dy)+','+str(x+dx)
                            if key in cube_active:
                                nbrs+=1
                key=str(z)+','+str(y)+','+str(x)
                if key in cube_active and (nbrs==2 or nbrs==3):
                    new_cube_active.add(key)
                elif key not in cube_active and nbrs==3:
                    new_cube_active.add(key)
    return new_cube_active
                        
def perf_cycle_4d(cube_active,n,dims):
    new_cube_active=set()
    
    for w in range(-n,dims[0]+n+1):
        for z in range(-n,dims[1]+n+1):
            for y in range(-n,dims[2]+n+1):
                for x in range(-n,dims[3]+n+1):
                    
                    nbrs=0
                    for dw in range(-1,2):
                        for dz in range(-1,2):
                            for dy in range(-1,2):
                                for dx in range(-1,2):
                                    if dw==0 and dz==0 and dy==0 and dx==0:
                                        continue
                                    key=str(w+dw)+','+str(z+dz)+','+str(y+dy)+','+str(x+dx)
                                    if key in cube_active:
                                        nbrs+=1
                    key=str(w)+','+str(z)+','+str(y)+','+str(x)
                    if key in cube_active and (nbrs==2 or nbrs==3):
                        new_cube_active.add(key)
                    elif key not in cube_active and nbrs==3:
                        new_cube_active.add(key)
    return new_cube_active
                         
                           
                

f = open("input.txt", "r")
cube_active3d=set()
cube_active4d=set()
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s=='#':
            cube_active3d.add('0,'+str(row)+','+str(col))
            cube_active4d.add('0,0,'+str(row)+','+str(col))  
f.close()

dims=[0,0,row,col]
for cycle in range(1,6+1):
    cube_active3d=perf_cycle_3d(cube_active3d,cycle,dims[1:])
    cube_active4d=perf_cycle_4d(cube_active4d,cycle,dims)


print("Part 1",len(cube_active3d))
print("Part 2",len(cube_active4d))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))