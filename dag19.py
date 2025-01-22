# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def match_rule(msg,i,rule_n,depth):
    rule=rules[rule_n]
    if rule_n==8:
        print('8')
    if rule_n==11:
        print('11')
    if i>=len(msg):
        print("te ver gezocht",i)
        return [False,i]
    #print(depth)
    #print(msg,depth,i,rule_n,msg[i])
    if rule=="a" or rule=="b":
        #print(msg[i]==rule)
        return [msg[i]==rule,i+1]
        
    elif '|' in rule:
        branches=rule.split('|')
        istart=i
        for branch in branches:
            valid=True
            new_rules = [int(d) for d in branch.split(',')]
            i=istart
            for new_rule in new_rules:
                [rtrn,i]= match_rule(msg,i,new_rule,depth+1)
                if rtrn==0:
                    valid=False
            if valid==True:
                #Hier moet hij nog branchen
                break
        #print("valid",valid)
                
    else:
        valid=True
        new_rules = [int(d) for d in rule.split(',')]
        for new_rule in new_rules:
            [rtrn,i]= match_rule(msg,i,new_rule,depth+1)
            if rtrn==0:
                valid=False
                break
            
            
    if depth>0:       
        return [valid,i]
    else:
        #print(len(msg),i)
        if len(msg)==i:
            return [valid,i]
        else:
            return [False,i]
        
        
def match_rule2(msg,i,rules_left,depth):
    if i==len(msg) and rules_left==[]:
        return True
    elif i>=len(msg):
        return False
    elif rules_left==[]:
        return False
    

    rule=rules[rules_left[0]]
    
    if rule=='a' or rule=='b':
        if msg[i]==rule:
            return match_rule2(msg,i+1,rules_left[1:],depth)
        else:
            return False
    elif '|' in rule:
        branches=rule.split('|')
        istart=i
        best=False
        for branch in branches:
            valid=True
            new_rules = [int(d) for d in branch.split(',')]
            rtrn = match_rule2(msg,i,new_rules+rules_left[1:],depth+1)
            if rtrn==True:
                best=True
        return best
    else:
        new_rules = [int(d) for d in rule.split(',')]
        return match_rule2(msg,i,new_rules+rules_left[1:],depth+1)
 


f = open("input.txt", "r")
rules=dict()
messages=list()
fase=0
for i,line in enumerate(f):
    if line=='\n':
        fase+=1
        continue
    line=line.replace('\n','').replace(' | ','|').replace(': ',':').replace(' ',',').replace('"','')
    
    if fase==0:
        rules.update({int(line.split(':')[0]):line.split(':')[1]})
    else:
        messages.append(line)

    
f.close()

total_p1=0
for message in messages:
    valid=match_rule2(message,0,[0],0)
    if valid==True:

        total_p1+=1

total_p2=0
rules[8]='42|42,8'
rules[11]='42,31|42,11,31'
for message in messages:
    valid=match_rule2(message,0,[0],0)
    if valid==True:
        total_p2+=1


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))