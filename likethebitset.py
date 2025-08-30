# binary string s of length n, int k
# construct a permutation p of length n 
# for each 1 <= i <= n, where si = 1
# each interval [l,r] (1<=l<=r<=n) whose length is at least k
# if l <= i <= r, the max among pl, pl+1,... , pr is not pi

# determine if such permutation exists
# find if there is k bits that are 1 in the string 
# since if there are more than k bits that are 0
# the interval [l,r] with length k always contains si = 1 
# which has pi and pi will always be maximum element 

import math
import sys

lines = sys.stdin.read().strip().split('\n')
t = int(lines[0])

for i in range(1, t*2, 2):
    nk = list(map(int, lines[i].split()))
    print(f"nk: {nk}")
    s = list(map(int, lines[i+1]))
    print(f"s: {s}")
    
    ones = s.count(1)
    print(f"ones: {ones}")
    if ones >= nk[1]:
        print("No")
    else:
        #permutation
        # for any bit sets length k that satisfies ones >= k
        # replace 
    
    













































































































