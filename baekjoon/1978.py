n = int(input())
cnt = 0
a,b,c,d = map(int,input().split())
for i in range(n):
    if a%2==1:
        cnt += 1
    if b%2==1:
        cnt +=1