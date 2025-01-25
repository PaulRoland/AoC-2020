# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
card_key,door_key=[int(d) for d in f.readlines()]
f.close()

card,card_ls,door,door_ls=[1,0,1,0]

sn=7
while card!=card_key:
    [card,card_ls]=[(card*7)%20201227,card_ls+1]

while door!=door_key:
    [door,door_ls]=[(door*7)%20201227,door_ls+1]

e_key=1
for _ in range(0,door_ls):
    e_key=(e_key*card_key)%20201227

print("Part 1",e_key)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))