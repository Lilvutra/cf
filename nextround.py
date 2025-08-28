input_str = input() #Input first line n,k
n, k = map(int, input_str.split())

count = 0 #Count the number of participants advancing to the next round
w = input()
numbers = w.split()
numbers = [int(num) for num in numbers]

for i in numbers:
    if i >= numbers[k-1] and i > 0:
        count += 1
    else:
        count == 0
print(count)



















