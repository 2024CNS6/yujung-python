n = int(input())
n1 = list(map(int,input().split()))
add = 0
for i in n1:
    if i % 5 == 0:
        add += i
print(add)