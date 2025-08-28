import sys




#Read input
num_cases = int(input())
for _ in range(num_cases):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    
def max_gcd(n, a):
    
    for i in range(len(a)):
        sorted = True
        if a[i] > a[i+1]:
            a[i] = a[i+1]
            a[i+1] = a[i]
            
            sorted = False
        if sorted:
            break
    return a 


    g = 0

    for k in range(1,n):
        g = math.gcd(g, a[k] - a[0])
    return g
            
            