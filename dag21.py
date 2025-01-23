# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
ingredients=list()
allergens=dict()
allergen_options=dict()
ingredient_list=dict()

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('\n','')
    
    ingredients=line.split(' contains ')[0].split(' ')
    allergens=line.split(' contains ')[1].split(', ')
    #print(ingredients,'\n',allergens)
    
    for ingredient in ingredients:
        if ingredient in ingredient_list:
            ingredient_list[ingredient]+=1
        else:
            ingredient_list.update({ingredient:1})
    
    for allergen in allergens:
        if allergen in allergen_options:
            allergen_options[allergen]=allergen_options[allergen].intersection(set(ingredients))
        else:
            allergen_options.update({allergen:set(ingredients)})
f.close()


ingredients_fixed=set()
while len(ingredients_fixed)<len(allergen_options):
    for allergen in allergen_options:
        difference=set(allergen_options[allergen])-ingredients_fixed
        #print(difference)
        if len(difference)==1:
            (diff,)=difference
            ingredients_fixed.add(diff)
            allergen_options[allergen]=diff
            print(allergen,diff)
total_p1=0        
for ingr in ingredient_list:
    if ingr in ingredients_fixed:
        continue
    total_p1+=ingredient_list[ingr]
    
allergens=list(allergen_options.keys())
allergens.sort()
total_p2=''
for key in allergens:
    total_p2+=allergen_options[key]+','
    
    


print("Part 1",total_p1)
print("Part 2",total_p2[:-1])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))