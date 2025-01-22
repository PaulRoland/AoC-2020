# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def match_rule(msg,i,rules_left,rules):
    if i==len(msg) and rules_left==[]:
        return True
    elif i>=len(msg):
        return False
    elif rules_left==[]:
        return False
    
    rule=rules[rules_left[0]]
    
    if rule=='a' or rule=='b': #Huidige regel is een vaste letter
        if msg[i]==rule:
            return match_rule(msg,i+1,rules_left[1:],rules)
        else:
            return False
        
    elif '|' in rule: #Huidige regel geeft een branch
        branches=rule.split('|')
        best=False
        for branch in branches:
            new_rules = [int(d) for d in branch.split(',')]
            rtrn = match_rule(msg,i,new_rules+rules_left[1:],rules)
            if rtrn==True:
                best=True
        return best
    
    else: #Huidige regel heeft nieuwe regels
        new_rules = [int(d) for d in rule.split(',')]
        return match_rule(msg,i,new_rules+rules_left[1:],rules)
 
    
f = open("input.txt", "r")
rules1=dict()
messages=list()
fase=0
for i,line in enumerate(f):
    if line=='\n':
        fase+=1
        continue
    line=line.replace('\n','').replace(' | ','|').replace(': ',':').replace(' ',',').replace('"','')
    if fase==0:
        rules1.update({int(line.split(':')[0]):line.split(':')[1]})
    else:
        messages.append(line)  
f.close()

rules2=dict(rules1)
rules2[8]='42|42,8'
rules2[11]='42,31|42,11,31'

total_p1=0
total_p2=0
for message in messages:
    total_p1+=match_rule(message,0,[0],rules1)
    total_p2+=match_rule(message,0,[0],rules2)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))