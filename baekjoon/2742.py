a,b,c = map(int,input().split())
while True:
    if a<b and a<c:
        print(a, end=' ')
        a = 1000000
    elif b<a and b<c:
        print(b, end=' ')
        b = 1000000
    elif c<b and c<a:
        print(c, end=' ')
        c = 1000000
    if a == 1000000 and b == 1000000 and c == 1000000:
        break