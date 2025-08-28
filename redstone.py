#Redstone

# n gears
# gear i has ai teeth
# spin the leftmost gear at a speed of 1 revolution per second
# for each of other gears, let x be the number of teeth it has 
# y be the number of teeth on the gear to its left
# z be the speed of the gear to its left spins at 
# its speed will be y/x * z revolutions per second

# the contraption is satisfactory if the rightmost gear spins at a speed of
# 1 revolution per second
# Determine if the contraption is satisfactory
import math
import sys 

lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])
print(f"t: {t}")

for i in range(1, t*2, 2):
    n = int(lines[i])
    gear_list = list(map(int, lines[i + 1].split()))
    
    if len(gear_list) != n:
        print("Error")   
    if len(gear_list) < 2:
        print("YES")
        
    print("YES") if set([x for x in gear_list if gear_list.count(x) > 1]) else print("NO")
           























