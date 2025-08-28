# First we get the number of lines n as the input 
# Loop through the number of
n = int(input()) 
count = 0
for i in range(0, n):
    x = input()
    if x.count('1') >= 2:
        count += 1
print(count)


