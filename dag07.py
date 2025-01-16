# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import re



def recurse_bag(upper_bag,new_bag,n):
    #memoization
    if new_bag in bag_total:
        for bag in bag_total[new_bag]:
            nbags= bag_total[new_bag][bag]
            if bag in bag_total[upper_bag]:
                bag_total[upper_bag][bag]+=n*nbags
            else:
                bag_total[upper_bag].update({bag:n*nbags})    
        return
    
    
    if new_bag=='':
        #Eerste level van de recursie
        bag_total.update({upper_bag:dict()})
        new_bag=upper_bag

    for bag in bag_description[new_bag]:
        nbags= bag_description[new_bag][bag]
        if bag in bag_total[upper_bag]:
            bag_total[upper_bag][bag]+=n*nbags
        else:
            bag_total[upper_bag].update({bag:n*nbags})
        recurse_bag(upper_bag,bag,n*nbags)
        
    return


bag_description=dict()
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')

    cur_bag=re.findall('[a-z ]* bags contain',line)[0][:-13]
    con_bags=re.findall('\d [a-zA-Z ]* bag',line)

    bag_description.update({cur_bag:dict()})
    for bag in con_bags:
        col=bag[2:-4]
        n=int(bag[0])
        bag_description[cur_bag].update({col:int(n)})
        
f.close()

#Extend the dict to contain every bag it containts etc etc
bag_total=dict()
for bag in bag_description:
    recurse_bag(bag,'',1)

total_p1=0   
total_p2=0 
for bag in bag_description:
    if 'shiny gold' in bag_total[bag]:
        total_p1+=1
        
for bag in bag_total['shiny gold']:
    total_p2+=bag_total['shiny gold'][bag]



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))