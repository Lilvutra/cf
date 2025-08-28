# n mobs stacked
# mob i has hi health
# 1 damage in 1 attack
# if any mob reaches 0 or less health, it dies and
# all the mobs above it fall down and form a new stack
# the bottom mob in the new stack takes 1 fall damage for each mob above it
# minimum attacks required to kill all the mobs 



import sys
import math

lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])

for i in range(1, t*2, 2):
    n = int(lines[i])
    health_list = list(map(int, lines[i + 1].split()))
    total_attacks = sum(health_list)
    #
    for i in range(n-1):
        total_attacks -= min()
    
    
    
    
    
    
    
    
    
    
    
    
    





















































