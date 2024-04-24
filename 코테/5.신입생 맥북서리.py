n,m = map(int,input().split())

m /= 60
n = float(n)
m = float(m)

if n >= 1000:
    n /= 1000
    print("%.2fkm/min"%(n/m))
else:
    print("%.2fm/min"%(n/m))