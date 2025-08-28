t = int(input()) # t: number of test cases 
results = []
for _ in range(t):
    # n: occupied time intervals 
    # s: time needed to take a shower
    # total minute a day has 
    n, s, m = map(int, input().split())
    
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
        
    intervals.sort()
    
    previous_end = 0
    result = "NO"
   
    for l, r in intervals:
        if l > previous_end:
            free_time = l - previous_end 
            #print(free_time)
        if free_time >= s:
            result = "YES"
        
        previous_end = r
        
    if previous_end < m:
        _free_time = m - previous_end 
        if _free_time >= s:
            result = "YES"
    results.append(result)

for res in results:
    print(res)