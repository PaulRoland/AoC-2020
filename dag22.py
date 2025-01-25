# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
from collections import deque
start_time = time.time_ns()

def crab_score(deck1,deck2):
    total=0
    i=0
    if len(deck2)==0:
        while len(deck_1)>0:
            i+=1
            total+=i*deck_1.pop()
    elif len(deck1)==0:
        while len(deck_2)>0:
            i+=1
            total+=i*deck_2.pop()
    return total

def rec_combat(deck1,deck2,mem,game):
    game_in_game=0
    rounds=0
    
    while len(deck1)!=0 and len(deck2)!=0:
        rounds+=1
        deck_key='1:'
        for d1,d2 in zip(deck1,deck2):
            deck_key+=str(d1)+','
        deck_key+=':2:'
        for d2 in deck2:
            deck_key+=str(d1)+','  
            
        if deck_key in mem:
           deck1.append(deck1.popleft())
           deck1.append(deck2.popleft())
           return [deck1,deck2,1]
        mem.update({deck_key:1})

        d1 = deck1.popleft()
        d2 = deck2.popleft()
        if d1<=len(deck1) and d2<=len(deck2):

            game_in_game+=1
            [_,_,win]=rec_combat(deque(list(deck1)[:d1]),deque(list(deck2)[:d2]),{},game+game_in_game)
            if win==1:
                deck1.append(d1)
                deck1.append(d2)
            else:
                deck2.append(d2)
                deck2.append(d1)
        else:
            if d1>d2:

                deck1.append(d1)
                deck1.append(d2)
            else:

                deck2.append(d2)
                deck2.append(d1)
    if len(deck1)==0:
        return [deck1,deck2,2]
    else:
        
        return [deck1,deck2,1]

f = open("input.txt", "r")
deck_1=deque()
deck_2=deque()

player=1
for i,line in enumerate(f):
    if line=='\n':
        player+=1
        continue
    if 'Player' in line:
        continue
    line=line.replace('\n','')
    if player==1:
        deck_1.append(int(line))
    else:
        deck_2.append(int(line))
f.close()
deck1=deque(list(deck_1))
deck2=deque(list(deck_2))
j=0
while len(deck_1)!=0 and len(deck_2)!=0:
    j+=1
    a=deck_1.popleft()
    b=deck_2.popleft()

    if a>b:
        deck_1.append(max(a,b))
        deck_1.append(min(a,b))
    else:
        deck_2.append(max(a,b))
        deck_2.append(min(a,b))

i=0
total_p1=crab_score(deck_1,deck_2)
[deck_1,deck_2,win]=rec_combat(deck1,deck2,{},1)
#print(deck1,deck2)
total_p2=crab_score(deck_1,deck2)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))