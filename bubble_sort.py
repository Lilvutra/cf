# n - number of elements 
# k - times passing through the list in bubble sort
# q - prime number for the output 

num_cases = int(input())
for i in range(num_cases):
    parts = input().split()
    n = int(parts[0])
    k = int(parts[1])
    q = int(parts[2])
    for j in range(k):
        A = [A[i] for i in range(1, n+1)]
        swapped = False
        for l in range(2, n):
            if A[l - 1] > A[l]:
                A[l - 1] == A[l]
                swapped = True
            count = 0
            if A[l - 1] < A[l]:
                count += 1
        lis = 0
        if count >= n - 1:
            lis += 1
almost_sorted_p = lis % q

for i in range(num_cases):
    print("Case #" + str(i) + ": " + str(almost_sorted_p))
            
            
        
            
            
                
            
            
            
            
  
    
   