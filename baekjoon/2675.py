n = int(input())
for i in range(n):
    m, s = input().split()
    s = list(s)
    m = int(m)
    for j in range(len(s)):
        print(s[j] * m, end='')
    print()