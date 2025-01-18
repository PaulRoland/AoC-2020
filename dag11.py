# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


seat_occ=set()
seat_emp=set()

f = open("input.txt", "r")
for row,line in enumerate(f):
    for col,s in enumerate(line):
        key=str(row)+','+str(col)
        if s=='L':
            seat_emp.add(key)
        elif s=='#':
            seat_occ.add(key)

f.close()

start_occ=set(seat_occ)
start_emp=set(seat_emp)

directions=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
changes=True
while changes==True:
    changes=False

    new_occ=set()
    new_emp=set()
    
    for key in seat_occ:
        [cr,cc]=[int(d) for d in key.split(',')]
        
        occ=0
        for [dr,dc] in directions:
            nkey=str(cr+dr)+','+str(cc+dc)
            if nkey in seat_occ:
                occ+=1
        if occ>=4:
            new_emp.add(key)
            changes=True
        else:
            new_occ.add(key)
            
    for key in seat_emp:
        [cr,cc]=[int(d) for d in key.split(',')]
        
        occ=0
        for [dr,dc] in directions:
            nkey=str(cr+dr)+','+str(cc+dc)
            if nkey in seat_occ:
                occ+=1
                break     
        if occ==0:
            new_occ.add(key)
            changes=True
        else:
            new_emp.add(key)
            
    seat_occ=set(new_occ)
    seat_emp=set(new_emp)

total_p1=len(seat_occ)
  

          
seat_occ=start_occ
seat_emp=start_emp
changes=True
while changes==True:
    changes=False

    new_occ=set()
    new_emp=set()
    
    for key in seat_occ:
        [cr,cc]=[int(d) for d in key.split(',')]
        
        occ=0
        for [dr,dc] in directions:
            for afstand in range(1,100):
                nkey=str(cr+dr*afstand)+','+str(cc+dc*afstand)
                if nkey in seat_occ:
                    occ+=1
                    break
                if nkey in seat_emp:
                    break
        if occ>=5:
            new_emp.add(key)
            changes=True
        else:
            new_occ.add(key)
            
    for key in seat_emp:
        [cr,cc]=[int(d) for d in key.split(',')]
        
        occ=0
        for [dr,dc] in directions:
            for afstand in range(1,100):
                nkey=str(cr+dr*afstand)+','+str(cc+dc*afstand)
                if nkey in seat_occ:
                    occ+=1
                    break
                if nkey in seat_emp:
                    break   
        if occ==0:
            new_occ.add(key)
            changes=True
        else:
            new_emp.add(key)
            
    seat_occ=set(new_occ)
    seat_emp=set(new_emp)

total_p2=len(seat_occ)
                        


                
            
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))