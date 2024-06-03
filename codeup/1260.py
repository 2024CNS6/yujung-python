a,b = map(int,input().split())
n = 0
for i in range(a,b+1):
    if i%3==0:
        n+=i
print(n)