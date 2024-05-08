s = input()

ck = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
n = 0

for i in ck:
    s = s.replace(i, '*')
print(len(s))