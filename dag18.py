# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def hw_eval(exp,i):
    value=0
    act='+'
    #print("new start")
    while i<len(exp):
        s = exp[i]
        i+=1
        if s==' ':
            continue
        if s==')':
            return [value,i]
        elif s=='(':
            [new_value,i]=hw_eval(exp,i)
        elif s.isdigit():
            new_value=int(s)
        else:
            act=s
            continue
        if act=='+':
            value+=new_value
        else:
            value*=new_value
    return [value,i]


def hw_eval_adv(exp,i):
    value=0
    act='+'
    while i<len(exp):
        s = exp[i]
        i+=1
        if s==' ':
            continue
        if s==')':
            return [value,i]
        elif s=='(':
            [new_value,i]=hw_eval_adv(exp,i)
        elif s.isdigit():
            new_value=int(s)
        elif s=='+':
            act='+'
            continue
        elif s=='*': #Eerst stuk achter de * evalueren
            act='*'
            [new_value,i]=hw_eval_adv(exp,i)
        if act=='+':
            value+=new_value
        else:
            #Na het afronden van een * de waarde returnen
            value*=new_value
            return [value,i]
    return [value,i]

            
total_p1=0
total_p2=0
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('\n','')
    total_p1+=hw_eval(line,0)[0]
    total_p2+=hw_eval_adv(line,0)[0]
        

    
f.close()

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))