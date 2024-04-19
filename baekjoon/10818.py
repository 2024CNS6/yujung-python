n = int(input())
for i in range(n):
    x = list(map(int,input().split()))
    print(min(x), end=' ')
    print(max(x))