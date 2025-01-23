# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def get_tile_info(start_row,end_row,col_left,col_right,tilestring):
    top=int(start_row,2)
    bot=int(end_row,2)
    left=int(col_left,2)
    right=int(col_right,2)
    topr=int(start_row[::-1],2)
    botr=int(end_row[::-1],2)
    leftr=int(col_left[::-1],2)
    rightr=int(col_right[::-1],2)       
    return [top,right,bot,left,topr,rightr,botr,leftr,tilestring]


def get_mirror_rotation(ind1,ind2):
    #ind1 = [0,1,2,3]  [U, R, D, L]
    #ind2 = [0,1,2,3,4,5,6,7] [U, R, D, L,Ur,Rr,Dr,Lr]
    
    #rot =  [0,1,2,3,0,1,2,3]
    #mir =  [0,0,0,0,1,1,1,1]
    grid=[
    [0,7,6,1,4,5,2,3],
    [1,0,7,6,3,4,5,2],
    [2,5,4,3,6,7,0,1],
    [3,2,5,4,1,6,7,0]]
    
    mirrot=grid[ind1].index(ind2)
    rot=mirrot%4
    mir=mirrot//4
    return [mir,rot]

def get_urdl(tile_info,mir,rot):
    #tile_info = [u,r,d,l,ur,rr,dr,lr]
    #mir =0/1
    #rot [0,1,2,3]
    mirrot=4*mir+rot
    grid=[
    [0,7,6,1,4,5,2,3],
    [1,0,7,6,3,4,5,2],
    [2,5,4,3,6,7,0,1],
    [3,2,5,4,1,6,7,0]]
    
    ui=grid[0][mirrot]
    ri=grid[1][mirrot]
    di=grid[2][mirrot]
    li=grid[3][mirrot]
    return [tile_info[ui],tile_info[ri],tile_info[di],tile_info[li]]

def image_mirror_rotate(image,mir,rot):
    #rotation cw, n*90
    if mir==1:
        max_c=len(image[0])
        max_r=len(image)
        new_image=[[[0] for _ in range(0,max_c)] for _ in range(0,max_r)]
        for r,line in enumerate(image):
            for c,s in enumerate(line):
                new_image[r][max_c-1-c]=s
        image=list(new_image)
    
    #Roteer n keer, 90
    for _ in range(0,rot):
        max_c=len(image[0])
        max_r=len(image)
        new_image=[[[0] for _ in range(0,max_r)] for _ in range(0,max_c)]
        for r,line in enumerate(image):
            for c,s in enumerate(line):
                new_image[c][max_c-1-r]=s
        image=list(new_image)
              
    output=list()
    for line in image:
        output.append(''.join(line))
    return output
    

f = open("input.txt", "r")
tiles=dict()
for i,line in enumerate(f):
    if line=='\n':
        tiles.update({tile_n:get_tile_info(start_row,end_row,col_left,col_right,tile_string)})
        continue
        
    line=line.replace('\n','').replace('#','1').replace('.','0')
    if 'Tile' in line:
        tile_n=int(line[5:-1])
        col_left=''
        col_right=''
        tile_row=0
        tile_string=list()
        continue
    
    col_left+=line[0]
    col_right+=line[-1]
    
    if tile_row==0:
        start_row=line
    elif tile_row==9:
        end_row=line
    else: #For part 2 get image without borders
        tile_string.append(line[1:-1])
        
    tile_row+=1
f.close()
top,right,bot,left,topr,rightr,botr,leftr,_=get_tile_info(start_row,end_row,col_left,col_right,tile_string)
tiles.update({tile_n:[top,right,bot,left,topr,rightr,botr,leftr,tile_string]})


puzzle=dict()
tile_placed=dict()

#Plaats het laatst gevonden stukje in normale orientatie om te beginnen
#row_col:ID,top,right,bot,left,mirror,rotation
puzzle.update({'0_0':[tile_n,top,right,bot,left,0,0]})
tile_placed.update({tile_n:'0_0'})

directions=[[-1,0],[0,1],[1,0],[0,-1]]
placed_counter=0
heap=list()

for [dr,dc],value,rot in zip(directions,[top,right,bot,left],[0,1,2,3]):
    heap.append([0,0,dr,dc,value,rot,tile_n])

i=0
counter_index=[2,3,0,1]
row_bounds=[-999,999]
col_bounds=[-999,999]
### Leg de puzzelstukjes
while i<len(heap):
    [cr,cc,dr,dc,value,rot_ind,tile_n]=heap[i]
    i+=1
    new_loc=str(cr+dr)+'_'+str(cc+dc)
    if new_loc in puzzle:
        #Hier is al een stukje
        continue
    
    #We moeten een vierkantje maken
    if cr+dr>row_bounds[1] or cr+dr<row_bounds[0]:
        continue
    if cc+dc>col_bounds[1] or cc+dc<col_bounds[0]:
        continue

    option_list=list()
    for new_tile in tiles:
        
        if new_tile in tile_placed:
            #Dit stukje hebben we al gehad
            continue

        new_tile_edges=tiles[new_tile][:-1]
        if value in new_tile_edges:
            rot_ind2=new_tile_edges.index(value)
            mir,rot=get_mirror_rotation(counter_index[rot_ind],rot_ind2)
            [nt,nr,nb,nl]=get_urdl(new_tile_edges,mir,rot)
            
            #Nog geen check of het echt past met de andere stukjes
            
            option_list.append([new_tile,nt,nr,nb,nl,mir,rot])
            
    if len(option_list)==0:
        #We moeten een vierkantje maken, dus als we een zij-/hoekstukje hebben veranderen de bounds
        if rot_ind==0:
            row_bounds[0]=cr
        elif rot_ind==2:
            row_bounds[1]=cr
        elif rot_ind==1:
            col_bounds[1]=cc
        elif rot_ind==3:
            col_bounds[0]=cc
        
    elif len(option_list)==1:
        #print("placed",option_list[0][0])
        puzzle.update({str(cr+dr)+'_'+str(cc+dc):option_list[0]})
        tile_placed.update({option_list[0][0]:str(cr+dr)+'_'+str(cc+dc)})
        for [ddr,ddc],value,rot in zip(directions,[nt,nr,nb,nl],[0,1,2,3]):
            heap.append([cr+dr,cc+dc,ddr,ddc,value,rot,option_list[0][0]])
        
    elif len(option_list)>1:
        print("multiple options")
        #Bekijk later nog een keer
        #heap.append([cr,cc,dr,dc,value,rot_ind])
  
### Vermenigvuldig de tile ID van de hoekpunten
total_p1=1     
for cr in row_bounds:
    for cc in col_bounds:
        key=str(cr)+'_'+str(cc)
        total_p1*=puzzle[key][0]
        
#Part 2
##Maak een dictonary van de locaties waar een monster moet zitten
monster=dict()            
sea_monster=['                  #','#    ##    ##    ###',' #  #  #  #  #  #   ']
for r,line in enumerate(sea_monster):
    for c,s in enumerate(line):
        if s=='#':
            monster.update({str(r)+','+str(c):[r,c]})
            
###Maak het totale plaatje aan de hand van part 1
total_image=list()
for cr in range(row_bounds[0],row_bounds[1]+1):
    new_rows=['' for _ in range(0,len(tile_string))]
    for cc in range(col_bounds[0],col_bounds[1]+1):
        key=str(cr)+'_'+str(cc)
        [mir,rot]=puzzle[key][-2:]
        cur_image=tiles[puzzle[key][0]][-1]
        add_to_rows=image_mirror_rotate(cur_image,mir,rot)
        for j,addition in enumerate(add_to_rows):
            new_rows[j]+=addition
    for line in new_rows:
        total_image.append(line.replace('1','#').replace('0',' '))

## P2 is aantal #, - # deel van een monster    
total_p2=0
for line in total_image:
    total_p2+=line.count('#')

#Try all orientations
monsters=0
monster_locs=set()
##Zoek in alle mirror/rotaties
for mir in [0,1]:
    for rot in [0,1,2,3]:
        match_image=image_mirror_rotate(total_image,mir,rot)

        #Probeer alle offsets
        for row_offset in range(0,len(match_image)-2):
            for col_offset in range(0,len(match_image[0])-19):
                has_monster=True
                for key in monster:
                    [r,c]=monster[key]
                    if match_image[row_offset+r][col_offset+c]=='#':
                        continue
                    else:
                        has_monster=False
                        break
                
                if has_monster==True:
                    for key in monster:
                        [r,c]=monster[key]   
                        monster_locs.add(str(r+row_offset)+','+str(c+col_offset))
                    monsters+=1
        #Gelukkig heeft maar een orientatie het patroon, dit is dus geen universele oplossing
        if monsters>0:
            for line in match_image:
                print(line)
            print('\n')
            for r,line in enumerate(match_image):
                new_line=''
                for c,s in enumerate(line):
                    if str(r)+','+str(c) in monster_locs:
                        new_line+='O'
                    else:
                        new_line+=s
                print(new_line)
            
            monsters=0
            total_p2-=len(monster_locs)
            break

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))