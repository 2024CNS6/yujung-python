min1,min2,min3,min4 = map(int,input().split())
man1,man2,man3,man4 = map(int,input().split())

minhap = (min1+min2+min3+min4)
manhap = (man1+man2+man3+man4)

if minhap > manhap:
    print(minhap)
elif minhap < manhap:
    print(manhap)
else:
    print(minhap)