# neither team score 3 consecutive goals in the same half
# Aquawave's team
# the score at the end of the first half was a : b
# the score at the end of the second half was c : d

# determine if Aquawave's dream can come true 
import sys
import math

lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])
print(f"t: {t}")

# neither s1 nor s2 contains 3
# 
for i in range(1, t + 1):
    print(f"i: {i}")
    score_list = list(map(int, lines[i].split()))
    print(f"score_list: {score_list}")
    
    print(f"score_list[0]: {score_list[0]}")
    print(f"score_list[2]: {score_list[2]}")
    
    
    if (max(score_list[0], score_list[1]) <= 2 * (min(score_list[0],score_list[1]) + 1)) and (max(score_list[2], score_list[3]) <=  2 * (min(score_list[2],score_list[3]) + 1)):
        print("Yes")
    else:
        print("No")
    
    
        
        






















