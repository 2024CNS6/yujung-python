n = []
for i in range(9):
    a = int(input())
    n.append(i)

print(max(n))
print(n.index(max(n)+1))