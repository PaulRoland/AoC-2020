# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def passport_validate(pp):
    checklist=['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for check in checklist:
        if check not in pp:
            return [0,0]
    
    
    byr_re =re.search(r'byr:\d{4} ',pp)
    if not byr_re: 
        print(re.search(r'byr:[a-Z]* ').group(0))
        return [0,1]
    byr = int(byr_re.group(0)[4:])
    if byr<1920 or byr>2002:
        print("byr invalid:",byr)
        return [0,1]
    
    
    iyr_re =re.search(r'iyr:\d{4}',pp)
    if not iyr_re: 
        print(re.search(r'iyr:[a-Z0-9]* ').group(0))
        return [0,1]
    iyr = int(iyr_re.group(0)[4:])
    if iyr<2010 or iyr>2020:
        print("iyr invalid:",iyr)
        return [0,1]
    
    eyr_re =re.search(r'eyr:\d{4}',pp)
    if not eyr_re:
        print(re.search(r'eyr:[a-Z0-9]* ').group(0))
        return [0,1]
    eyr = int(eyr_re.group(0)[4:])
    if eyr<2020 or eyr>2030:
        print("eyr invalid:",eyr)
        return [0,1]
    
    hgt_re =re.search(r'hgt:\d{3}cm',pp)
    if hgt_re:
        hgt=int(hgt_re.group(0)[4:7])
        if hgt<150 or hgt>193:
            print("Wrong height",hgt,"cm")
            return [0,1]
    else:
        hgt_re =re.search(r'hgt:\d{2}in',pp)
        if hgt_re:
            hgt=int(hgt_re.group(0)[4:6])
            if hgt<59 or hgt>76:
                print("Wrong height",hgt,"in")
                return [0,1]    
        else:
            return [0,1]
        
    hcl_re =re.search(r'hcl:#[0-9a-fA-F]{6} ',pp)
    if not hcl_re:
        return [0,1]
     
    ecl_re =re.search(r'ecl:[abgho][mlrzt][bunylh] ',pp)
    if not ecl_re:
        print("ECL, wrong re")
        return [0,1]
    ecl = ecl_re.group(0)[4:7]
    if ecl not in ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print("ECL wrong, re good",ecl)
        return [0,1]
    
    pid_re =re.search(r'pid:[0-9]{9} ',pp) 
    if not pid_re:
        print(re.search(r'pid:[#a-zA-Z0-9]*',pp).group(0) )
        #print(pp)
        return [0,1]
    
    return [1,1]
    

f = open("input.txt", "r")
data=''
valid_ps=0
passports=list()
for i,line in enumerate(f):
    if line=='\n':
        passports.append(data)
        data=''
        continue
    
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data+=line+' '  
f.close()
passports.append(data)

total_p1=0
total_p2=0
for passport in passports:
    [p2,p1] = passport_validate(passport)
    total_p1+=p1
    total_p2+=p2

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))