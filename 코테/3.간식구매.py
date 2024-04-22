n = input()
m = int(input())
num = 0
for i in range(m):
    name = list(input())
    num += 1
    if name[0]==n or name[1]==n or name[2]==n:
        num += 1
print(num)