# t - the number of test cases 
# n,k - the requested year and the numer of years during which the leaves remain
# grows i^i new leaves in the i-th year


num_cases = int(input())

for i in range(num_cases):
    input = list(map(int, input().split()))
     
    if input[1] == 1 and (input[0] // 2) == 0:
        print('YES, EVEN')
    if (input[1] // 2) != 0 and (input[0] // 2) != 0:
        print("YES, EVEN")
    if (input[1] // 2) == 0 and input[1] > 4 and input[0] > 2:
        print("NO, ODD")
    else:
        print("NO, ODD")
    
        
        
    
    # if k is odd:
    #     only even at odd years
    # if k is even and k < 4 and n > 2:
    #     only odd
    
        
















