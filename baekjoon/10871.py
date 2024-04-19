x, y = list(map(int,input().split()))
n = list(map(int,input().split()))
for i in range(x):
    if n[i] < y:
        print(n[i], end=" ")
