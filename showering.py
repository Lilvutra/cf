t = int(input()) 
for _ in range(t):
    n, s, m = map(int, input().split())
    
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))

    intervals.sort()
    previous_end = 0
    result = 'NO'
    
    # Calculate the free time between intervals
    for l, r in intervals:
        # Free time before the current interval starts
        if l > previous_end:
            free_time = l - previous_end
        if free_time > s:
            result = 'YES'
        # Update the end of the previous interval
        previous_end = r
    
    if previous_end < m:
        l_free_time = m - previous_end
        if l_free_time > s:
            result = 'YES'
    print(result)
        
        
# R=lambda:map(int,input().split())
# t,=R()
# while t:
#  t-=1;n,s,m=R();a=[0]
#  while n:n-=1;a+=R()
#  print('YNEOS'[all(y-x<s for x,y in zip(a[::2],a[1::2]+[m]))::2])
