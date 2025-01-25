# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import matplotlib.pyplot as plt
start_time = time.time_ns()

def parse_hex(string):
    hex_move={'ne':[1,1],'nw':[1,0],'e':[0,1],'se':[-1,0],'sw':[-1,-1],'w':[0,-1]}
    i=0
    hy=0
    hx=0
    while i<len(string):
        if i<len(string)-1:
            substring=string[i:i+2]
            if substring in hex_move:
                hy+=hex_move[substring][0]
                hx+=hex_move[substring][1]
                i+=2
                continue
        substring=string[i]
        if substring in hex_move:
            hy+=hex_move[substring][0]
            hx+=hex_move[substring][1]
            i+=1
            continue
    return [hy,hx]


def draw_hex(tiles):
    plt.figure(figsize=(12,12))
    for tile in tiles:
        if tiles[tile]==False:
            continue
        
        [hy,hx]=[int(d) for d in tile.split(',')]
        [y,x]=[hy*3,hy*-2]
        x+=hx*4
        
        contour=[y+2,x,y+1,x+2,y-1,x+2,y-2,x,y-1,x-2,y+1,x-2]
        c_x=contour[1::2]
        c_y=contour[0::2]
        plt.fill(c_x,c_y,facecolor='k')
        plt.axis([-220,220,-200,200])
    plt.show()
        
f = open("input.txt", "r")
tiles_flipped=dict()
bounds=[0,0,0,0]
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [hy,hx]=parse_hex(line)
    key=str(hy)+','+str(hx)
    bounds=[min(bounds[0],hy),max(bounds[1],hy),min(bounds[2],hx),max(bounds[3],hx)]
    if key in tiles_flipped:
        tiles_flipped[key]=not tiles_flipped[key]
    else:
        tiles_flipped[key]=True
f.close()


total_p1=0

for key in tiles_flipped:
    if tiles_flipped[key]==True:
        total_p1+=1

#part 2
n_days=100

for chy in range(bounds[0]-n_days-3,bounds[1]+n_days+3):
    for chx in range(bounds[2]-n_days-3,bounds[3]+n_days+3):
        key=str(chy)+','+str(chx)
        if key in tiles_flipped:
            continue
        tiles_flipped.update({key:False})

for days in range(1,1+n_days):
    new_tiles_flipped=dict(tiles_flipped)
    for chy in range(bounds[0]-days,bounds[1]+days+1):
        for chx in range(bounds[2]-days,bounds[3]+days+1):
            black_tiles=0
            for [dhy,dhx] in [[1,1],[1,0],[0,1],[-1,0],[-1,-1],[0,-1]]:
                key=str(chy+dhy)+','+str(chx+dhx)
                black_tiles+=tiles_flipped[key]
                
            key=str(chy)+','+str(chx)
            new_tiles_flipped.update({key:False})

            cur_tile=tiles_flipped[key]

            if cur_tile==True:
                new_tiles_flipped[key]=not (black_tiles==0 or black_tiles>2)
            else:
               new_tiles_flipped[key]=(black_tiles==2)
               
    tiles_flipped=dict(new_tiles_flipped)   
    #draw_hex(tiles_flipped)
total_p2=0
for key in tiles_flipped:
    if tiles_flipped[key]==True:
        total_p2+=1                        
            
            



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))