#villagers

# n villagers 
# villager i has a grumpiness level of ai
# select two villagers i and j and give them max(gi, gj)
# their grumpiness decreases by min(gi, gj)
# and they become friends with each other 

import math 
import sys 

# Approach:
# If there are two or more villagers with the same grumpiness level,
# we can always make the grumpiness of all villagers zero.
# If all villagers have distinct grumpiness levels, it is impossible
# to make the grumpiness of all villagers zero. 

# wanna find way to spend the least emeralds 
# if number of villagers is 2, max(g1,g2) is the answer
# if number of villagers is > 2, we can find the min emeralds by 
# a1,a2,a3,...,an -> 
# if an is odd, 

lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])
print(f"t: {t}")

for i in range(1, t*2, 2):
    n = int(lines[i])
    grumpiness_list = list(map(int, lines[i + 1].split()))
    
    if len(grumpiness_list) != n:
        print("Error")   
    if len(grumpiness_list) < 2:
        print(max(grumpiness_list[0], grumpiness_list[1]))
    total_emeralds = 0
    stack = sorted(grumpiness_list)
    #Choose every second largest element
    while len(stack) > 1:
        g1 = stack.pop(0)
        g2 = stack.pop()
        total_emeralds += max(g1, g2)
        new_g1 = g1 - min(g1,g2)
        new_g2 = g2 - min(g1,g2)
    if new_g1 > 0:
        stack.append(new_g1)
    if new_g2 > 0:
        stack.append(new_g2)
    stack.sort()
    print(total_emeralds)
        
        
        


































