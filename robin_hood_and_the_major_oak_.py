num_cases = int(input())

for _ in range(num_cases):
    n, k = map(int, input().split())
    
    # Start and end of the range
    start = n - k + 1
    end = n
    
    # Count how many odd numbers are in the range [start, end]
    odd_count = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            odd_count += 1
    
    # If the number of odd terms is odd, the sum is odd, otherwise it's even
    if odd_count % 2 == 0:
        print("YES")
    else:
        print("NO")
