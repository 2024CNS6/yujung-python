n = int(input())
s = 0

for i in range(1, n+1):
    s+=i
print(s)
m = 0

m += s*s
print(m)
s = 0

for i in range(1, n+1):
    s += i*i*i
print(s)