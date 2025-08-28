n = int(input())
X = 0
for i in range(0,n):
    w = input()
    if w.count("++X") == 1 or w.count("X++") == 1:
        X += 1 
    if w.count("--X") == 1 or w.count("X--") == 1:
        X -= 1
print(X)














