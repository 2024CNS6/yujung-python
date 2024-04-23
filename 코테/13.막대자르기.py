n = int(input())
bar = 0
barlen = 0
min = 32
while barlen != n:
    if n-barlen >= min:
        barlen += min
        bar += 1
    min /= 2
    if min < 1:
        break
print(bar)