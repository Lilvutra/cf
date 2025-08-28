import sys
l, r = 1, 1000000
print(r)
while l < r:
    mid = (l+r+1)/2
    print(mid)
    sys.stdout.flush()
    response = input().strip()
    if response == '<':
        r = mid - 1
    elif response == ">=":
        l = mid
        
print(l)
sys.stdout.flush()
