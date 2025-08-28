from itertools import permutations

def longest_increasing_subsequence_length(sequence):
    if not sequence:
        return 0
    n = len(sequence)
    # Create a list to store the length of LIS ending at each index
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)

def bubble_sort_once(arr):
    swapped = False #Track whether any elements are sorted
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    return swapped

num_cases = int(input())
for case_number in range(1, num_cases + 1):
    n, k, q = map(int, input().split())
    
    all_permutations = list(permutations(range(1, n + 1)))
    print(all_permutations)
    almost_sorted_count = 0
    
    for perm in all_permutations:
        A = list(perm)
        print(A)
        for _ in range(k):
            if not bubble_sort_once(A):
                break
        
        # Check if the permutation is almost sorted
        if longest_increasing_subsequence_length(A) >= n - 1:
            almost_sorted_count += 1
    
    almost_sorted_p = almost_sorted_count % q
    print(f"Case #{case_number}: {almost_sorted_p}")
