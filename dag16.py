# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def combine_ranges(ranges1,ranges2):
    if len(ranges1)==0:
        return ranges2
    if len(ranges2)==0:
        return ranges1

    combined_ranges=ranges1
    new_low=0
    for low,high in zip(ranges2[::2],ranges2[1::2]):
        new_combined_ranges=list()

        going=False
        if low==max(combined_ranges)+1:
            combined_ranges[-1]=high
            continue
        if low>max(combined_ranges):
            combined_ranges.extend([low,high])
            continue
        
        for i,[low2,high2] in enumerate(zip(combined_ranges[::2],combined_ranges[1::2])):

            if going==True:
                if high<low2:
                   new_combined_ranges.extend([new_low,high])
                   new_combined_ranges.extend(combined_ranges[i*2:])
                   going=False
                   break
                elif high>low2 and high<=high2:
                   new_combined_ranges.extend([new_low,high2])
                   new_combined_ranges.extend(combined_ranges[i*2+2:])
                   going=False
                   break
                continue      
            #0
            if high<low2:
                new_combined_ranges.extend([low,high])
                new_combined_ranges.extend(combined_ranges[i*2:])
                break
            #1
            if low<low2 and high>low2 and high<high2:
                print(low,low2,high,high2)
                new_combined_ranges.extend([low,high2])
                
                new_combined_ranges.extend(combined_ranges[i*2+2:])
                print(new_combined_ranges)
                break         
            #2
            if low<low2 and high>high2:
                new_low=low
                going=True
                continue
            #3
            if low>=low2 and low<=high2 and high>high2:
                new_low=low2
                going=True
                continue
            #4
            if low>=low2 and high<=high2:
                new_combined_ranges.extend([low2,high2])
            #5
            if low>=high2:
                new_combined_ranges.extend([low2,high2])

        if going==True:
            new_combined_ranges.extend([new_low,high])
        
        combined_ranges=list(new_combined_ranges)  
    return combined_ranges

def value_in_ranges(value,ranges):
    for low,high in zip(ranges[::2],ranges[1::2]):
        if value>=low and value<=high:
            return 1
    return 0


f = open("input.txt", "r")
fase=1
tickets_near=list()
ranges=dict()
all_ranges=list()
for i,line in enumerate(f):
    if line=='\n':
        fase+=1
        continue
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    
    if fase==1:
        key=line.split(':')[0]
        new_range=[int(d) for d in re.findall('\d+',line)]
        ranges.update({key:new_range})
        all_ranges=combine_ranges(all_ranges,new_range)
    elif fase==2:
        if 'your' in line:
            continue
        your_ticket=[int(d) for d in line.split(',')]
    elif fase==3:
        if 'nearby' in line:
            continue
        tickets_near.append([int(d) for d in line.split(',')])
     
f.close()

total_p1=0
tickets_p2=list()
for ticket in tickets_near:
    good=True
    for value in ticket:
        if value_in_ranges(value,all_ranges):
            continue
        total_p1+=value
        good=False
    if good==True:
        tickets_p2.append(ticket)
        

opties=dict()
for key in ranges:
    ranges1=ranges[key]
    opties.update({key:[]})
    for i in range(0,len(your_ticket)):
        good=True
        for ticket in tickets_p2:
            if value_in_ranges(ticket[i],ranges1)==0:
                good=False
                break
        if good==True:
            opties[key].append(i)
            

counter=0
fixed=dict()
while len(fixed)<len(your_ticket):
    for key in opties:
        if len(opties[key])==1:
            removal=opties[key][0]
            fixed.update({key:removal})
            del opties[key]
            break
        
    for key in opties:
        if removal in opties[key]:
            opties[key].remove(removal)
   
total_p2=1            
for key in fixed:
    if 'departure' in key:
        total_p2*=your_ticket[fixed[key]]
        


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))