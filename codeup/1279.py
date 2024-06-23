n = list(map(int,input().split()))
add = 0
for i in range(min(n),max(n)+1):
    if i%2==0:
        add-=i
    else:
        add+=i
print(add)