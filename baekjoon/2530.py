a,b,c = map(int,input().split())
n = int(input())
b+=n//60
c+=n%60
while True:
    if c>=60:
        c-=60
        b += 1
    elif b>=60:
        b-=60
        a+=1
    elif a>=24:
        a-=24
    elif c<60 and b<60:
        break
print(a,b,c)