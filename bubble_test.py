
def longest_increasing_subsequence_length(sequence):
    if not sequence:
        return 0
    n = len(sequence)
    print(n)
    # Create a list to store the length of LIS ending at each index
    lis = [1] * n
    print(lis)
    for i in range(1, n):
        print(i)
        for j in range(i):
            print(j)
            if sequence[i] > sequence[j]:

                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)
print(longest_increasing_subsequence_length([5, 4, 3, 2, 1]))

def get_permutations(sequence):
    # Base case: if the sequence is empty or has one element, return it as the only permutation
    if len(sequence) == 0:
        return [[]]  # Return a list containing an empty list (base case for permutations)
    if len(sequence) == 1:
        return [sequence]  # Return a list containing the single element sequence
    
    permutations = []
    for i in range(len(sequence)):
        # Choose the current element
        element = sequence[i]
        # Generate permutations of the remaining elements
        remaining = sequence[:i] + sequence[i+1:]
        print("remains" + str(remaining))
        for perm in get_permutations(remaining):
            print("perms" + str(perm))
            # Combine the chosen element with each permutation of the remaining elements
            permutations.append([element] + perm)
    
    return permutations

# Example usage:
sequence = [1, 2, 3]
perms = get_permutations(sequence)
for perm in perms:
    print(perm)
