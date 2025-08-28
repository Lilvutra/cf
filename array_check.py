# check if array is increasing
arr = [1, 2, 3]
for i in range(len(arr)):
    print(f"i: {i}")
    j = len(arr) - i + 1 
    if arr[j] > arr[i]:
        print("array is increasing")
        