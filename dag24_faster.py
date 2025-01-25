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
        [hy,hx]=[int(d) for d in tile.split(',')]
        [y,x]=[hy*3,hy*-2]
        x+=hx*4
        
        contour=[y+2,x,y+1,x+2,y-1,x+2,y-2,x,y-1,x-2,y+1,x-2]
        c_x=contour[1::2]
        c_y=contour[0::2]
        plt.fill(c_x,c_y,facecolor='k')
        plt.axis([-220,220,-200,200])
    plt.show()
        
f = open("test.txt", "r")
black_tiles=set()
bounds=[0,0,0,0]
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [hy,hx]=parse_hex(line)
    key=str(hy)+','+str(hx)
    bounds=[min(bounds[0],hy),max(bounds[1],hy),min(bounds[2],hx),max(bounds[3],hx)]
    if key in black_tiles:
        black_tiles.remove(key)
    else:
        black_tiles.add(key)
f.close()


total_p1=len(black_tiles)

#part 2
n_days=100

for days in range(1,1+n_days):
    new_black_tiles=set()
    black_tile_nbrs=dict()    
    
    for tile in black_tiles:
        
        [chy,chx]=[int(d) for d in tile.split(',')]
        key=str(chy)+','+str(chx)
        if key in black_tile_nbrs:
            black_tile_nbrs[key][0]=1
        else:
            black_tile_nbrs.update({key:[1,0]})
            
        for [dhy,dhx] in [[1,1],[1,0],[0,1],[-1,0],[-1,-1],[0,-1]]:
            key=str(chy+dhy)+','+str(chx+dhx)
            if key in black_tile_nbrs:
                black_tile_nbrs[key][1]+=1
            else:
                black_tile_nbrs.update({key:[0,1]})
    
    for tile in black_tile_nbrs:
        [chy,chx]=[int(d) for d in tile.split(',')]

        if black_tile_nbrs[tile][0]==1 and (black_tile_nbrs[tile][1]==1 or black_tile_nbrs[tile][1]==2):
            new_black_tiles.add(tile)
        elif black_tile_nbrs[tile][0]==0 and black_tile_nbrs[tile][1]==2:
            new_black_tiles.add(tile)
               
    black_tiles=set(new_black_tiles)

    #draw_hex(black_tiles)
total_p2=len(black_tiles)                 
            
            



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))