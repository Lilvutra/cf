""" Int m
Int n - n integers Zi
Integers Zi

For each Zi —> pairs x,y (0 <=x, y<m) such that x^2 + y^2 = Zi (mod m)


Three cases:

Zi mod m 

- If Zi < m —> Zi mod m = Zi 
- + 
- If Zi > m —> Zi mod m(Suppose Zi mod m = Zi - m)
- + 
- If Zi = m —> Zi mod m = 0 
- + 
- Square sum:
- 2 = 1^2 + 1^2 
- 2 = (-1)^2 + (-1)^1 
- 1 = 0^1 + 1^2
- 1 = 1^2 + 0^1

num_pairs = 0
- For i in range(Zi % m)
- If i^2 + i^2 = Zi  % m 
- num_pairs += 2(permutation)  """

import sys

print("Enter input: ")
# all_input = sys.stdin.read().split("\\")
all_input = sys.stdin.read().splitlines()
print(f"all_input: {all_input}")
print(type(all_input))

# Separate the list 
line0 = list(map(int, all_input[0].split()))
print(f"line0: {line0}")
line1 = list(map(int, all_input[1].split()))
print(f"line1: {line1}")

if len(line1) != line0[1]:
    print("invalid input")
    
pair_count_list = []
for i in line1:
    pair_count = 0
    mod_r = i % line0[1]
    print(f"mod_r: {mod_r}")
    print(f"range(mod_r): {range(mod_r)}")
    if mod_r == 0:
        pair_count += 1 
        pair_count_list.append(pair_count)
        print(f"pair_count_list(mod_r != 0): {pair_count_list}")
    if mod_r != 0:
        for k in range(mod_r):
            print(f"k: {k}")
            if (k**2 + k**2) == mod_r:
                pair_count += 4
            if (k**2 + (k+1)**2) == mod_r:
                pair_count += 4
        pair_count
        print(f"pair_count: {pair_count}")
        pair_count_list.append(pair_count)
        print(f"pair_count_list: {pair_count_list}")